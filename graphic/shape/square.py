from .shape import Shape
from ..drawer import Color
# from graphic.scene import Scene
# from graphic.shape import Point2D, Line


class Square(Shape):
    square_counter = 0

    def __init__(self, start, w, h, drawer, color=None):
        Shape.__init__(self, drawer)
        self.start = start
        self.w = w
        self.h = h
        self.square_counter += 1
        self.color = color or Color(255, 255, 255)

    @staticmethod
    def stat():
        print(f"{Square.square_counter} was created")

    def draw(self):
        pass
        # x = self.start.x
        # y = self.start.y
        # for i in range(0, self.h+1):
        #     p_start = Point2D(x, y+i, drawer=self.drawer)
        #     p_end = Point2D(x+self.w, y+i, drawer=self.drawer)
        #     Scene().add(Line(p_start, p_end, self.drawer, color=self.color))
