from figures.intersection import Intersection
from figures.ray import Ray
from physical.material import Material
from physical.point_light import Light
from features.point import Point
from features.vector import Vector
from features.color import Color, BLACK_COLOR
from physical.world import World
from figures.computation import Computation
from math import pow

class Shader():

    @staticmethod
    def lighting(material: Material, light: Light, point: Point, eyev: Vector, normalv: Vector, in_shadow: bool) -> Color:
        if material.pattern != None:
            color = material.pattern.color_at(point)
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
    def shade_hit(world: World, comp: Computation) -> Color:
        is_shadowed = Shader.is_shadowed(world, comp.over_point)
        return Shader.lighting(comp.object.material, world.light, comp.point, comp.eyev, comp.normalv, is_shadowed)

    @staticmethod
    def color_at(world: World, ray: Ray) -> Color:
        intersections = Intersection.find_intersections_of_ray_and_world(ray, world)
        hit = Intersection.calculate_hit_from_sorted_intersections(intersections)
        if hit == None:
            return BLACK_COLOR
        comps = hit.prepare_computation(ray)
        return Shader.shade_hit(world, comps)
    
    @staticmethod
    def is_shadowed(world: World, point: Point) -> bool:
        v = Vector.fromtuple(world.light.position - point)
        distance = v.magnitude()
        direction = v.normalize()
        r = Ray(point, direction)
        intersections = Intersection.find_intersections_of_ray_and_world(r, world)
        h = Intersection.calculate_hit(intersections)
        return h != None and h.t < distance