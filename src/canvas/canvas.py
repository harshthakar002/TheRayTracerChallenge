from features.color import color

class canvas():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.pixels = [[color(0, 0, 0)] * height] * width