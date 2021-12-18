from figures.shape import Shape

class Group(Shape):

    def __init__(self) -> None:
        super().__init__()
        self.shapes = []

    def is_empty(self) -> bool:
        return len(self.shapes) == 0