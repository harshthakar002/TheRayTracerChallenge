from features.color import color

class canvas():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.pixels = []
        for i in range(height):
            self.pixels.append([])
            for j in range(width):
                self.pixels[i].append(color(0, 0, 0))
    
    def write_pixel(self, x: int, y: int, c: color) -> None:
        self.pixels[y][x] = c
    
    def pixel_at(self, x: int, y: int) -> color:
        return self.pixels[y][x]