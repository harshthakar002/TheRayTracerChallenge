from features.color import Color

class Material():

    def __init__(self, color=Color(1, 1, 1), ambient=0.1, diffuse=0.9, specular=0.9, shininess=200.0) -> None:
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess