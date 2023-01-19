from .shape import Shape
from ..drawer import Color


class Circle(Shape):
    circle_counter = 0

    def __init__(self, x, y, r, drawer, color=None):
        Shape.__init__(self, drawer)
        self.x_c = x
        self.y_c = y
        self.r = r
        self.circle_counter += 1
        self.color = color or Color(255, 255, 255)

    @staticmethod
    def stat():
        print(f'{Circle.circle_counter} was created')

    def draw(self):
        disp_x = self.x_c
        disp_y = self.y_c
        x = 0
        y = self.r
        delta = 1 - 2 * self.r
        while y >= 0:
            self.drawer.put_pixel(disp_x + x, disp_y + y, self.color)
            self.drawer.put_pixel(disp_x + x, disp_y - y, self.color)
            self.drawer.put_pixel(disp_x - x, disp_y + y, self.color)
            self.drawer.put_pixel(disp_x - x, disp_y - y, self.color)
            error = 2 * (delta + y) - 1
            if delta < 0 and error <= 0:
                x += 1
                delta = delta + (2 * x + 1)
                continue
            if delta > 0 and error > 0:
                y -= 1
                delta = delta + (1 - 2 * y)
                continue
            x += 1
            delta = delta + (2 * (x - y))
            y -= 1
