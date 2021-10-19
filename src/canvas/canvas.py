from features.color import color

class canvas():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.pixels = [[color(0, 0, 0)] * height] * width
    
    def write_pixel(self, x: int, y: int, c: color) -> None:
        self.pixels[x][y] = c
    
    def pixel_at(self, x: int, y: int) -> color:
        return self.pixels[x][y]