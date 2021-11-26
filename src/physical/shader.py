from figures.intersection import Intersection
from figures.ray import Ray
from physical.material import Material
from physical.point_light import Light
from features.point import Point
from features.vector import Vector
from features.color import WHITE_COLOR, Color, BLACK_COLOR
from physical.world import World
from figures.computation import Computation
from math import pow, sqrt
from figures.figure import Figure
from features.equality import is_approximately_equal

class Shader():

    @staticmethod
    def lighting(material: Material, object: Figure, light: Light, point: Point, eyev: Vector, normalv: Vector, in_shadow: bool) -> Color:
        if material.pattern != None:
            color = material.pattern.color_at_object_point(object, point)
        else:
            color = material.color
        effective_color = Color(color.red * light.intensity.red, color.green * light.intensity.green, color.blue * light.intensity.blue)
        light_vector = Vector(light.position.x - point.x, light.position.y - point.y, light.position.z - point.z).normalize()
        ambient = effective_color * material.ambient

        if in_shadow:
            return ambient
        light_dot_normal = light_vector.dotProduct(normalv)
        if light_dot_normal < 0:
            diffuse = BLACK_COLOR
            specular = BLACK_COLOR
        else:
            diffuse = effective_color * (material.diffuse * light_dot_normal)
        
        reflectv = light_vector.negate().reflect(normalv)
        reflect_dot_eye = reflectv.dotProduct(eyev)

        if reflect_dot_eye <= 0:
            specular = BLACK_COLOR
        else:
            factor = pow(reflect_dot_eye, material.shininess)
            specular = light.intensity * (material.specular * factor)

        return ambient + diffuse + specular

    @staticmethod
    def shade_hit(world: World, comp: Computation, remaining: int) -> Color:
        is_shadowed = Shader.is_shadowed(world, comp.over_point)
        surface = Shader.lighting(comp.object.material, comp.object, world.light, comp.point, comp.eyev, comp.normalv, is_shadowed)
        reflected_color = Shader.reflected_color(world, comp, remaining)
        refracted_color = Shader.refracted_color(world, comp, remaining)
        material = comp.object.material
        if material.reflective > 0 and material.transparency > 0:
            reflectance = comp.schlick()
            return surface + (reflected_color * reflectance) + (refracted_color * (1 - reflectance))
        return surface + reflected_color + refracted_color

    @staticmethod
    def color_at(world: World, ray: Ray, remaining: int) -> Color:
        intersections = Intersection.find_intersections_of_ray_and_world(ray, world)
        hit = Intersection.calculate_hit_from_sorted_intersections(intersections)
        if hit == None:
            return BLACK_COLOR
        comps = hit.prepare_computation(ray, intersections)
        return Shader.shade_hit(world, comps, remaining)
    
    @staticmethod
    def is_shadowed(world: World, point: Point) -> bool:
        v = Vector.fromtuple(world.light.position - point)
        distance = v.magnitude()
        direction = v.normalize()
        r = Ray(point, direction)
        intersections = Intersection.find_intersections_of_ray_and_world(r, world)
        h = Intersection.calculate_hit(intersections)
        return h != None and h.t < distance
    
    @staticmethod
    def refracted_color(world: World, comps: Computation, remaining: int) -> Color:
        if is_approximately_equal(comps.object.material.transparency, 0) or remaining <= 0:
            return BLACK_COLOR
        n_ratio = comps.n1 / comps.n2
        cos_i = comps.eyev.dotProduct(comps.normalv)
        sin2_t = (n_ratio * n_ratio) * (1 - (cos_i * cos_i))
        if sin2_t > 1:
            return BLACK_COLOR
        cos_t = sqrt(1.0 - sin2_t)
        direction = Vector.fromtuple((comps.normalv * ((n_ratio * cos_i) - cos_t)) - (comps.eyev * n_ratio))
        refract_ray = Ray(comps.under_point, direction)
        return Shader.color_at(world, refract_ray, remaining - 1) * comps.object.material.transparency
    
    @staticmethod
    def reflected_color(world: World, comps: Computation, remaining: int) -> Color:
        if is_approximately_equal(comps.object.material.reflective, 0.0) or remaining <= 0:
            return BLACK_COLOR
        reflect_ray = Ray(comps.over_point, comps.reflectv)
        color = Shader.color_at(world, reflect_ray, remaining - 1)
        return color * comps.object.material.reflective