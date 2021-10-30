from physical.material import Material
from physical.point_light import Light
from features.point import Point
from features.vector import Vector
from features.color import Color, BLACK_COLOR
from math import pow

class Lighter():

    @staticmethod
    def lighting(material: Material, light: Light, point: Point, eyev: Vector, normalv: Vector) -> Color:
        effective_color = Color(material.color.red * light.intensity.red, material.color.green * light.intensity.green, material.color.blue * light.intensity.blue)
        light_vector = Vector(light.position.x - point.x, light.position.y - point.y, light.position.z - point.z).normalize()
        ambient = effective_color * material.ambient
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