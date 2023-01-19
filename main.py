import random
from math import sqrt

from graphic.scene import Scene
from graphic.drawer import Drawer, Color
from graphic.shape import Point2D, Line, Circle, Square


def main(name_of_figure='line', x_c=0, y_c=0, rad=0, w=0, h=0, r=0, g=0, b=0):

    s = Scene()

    if name_of_figure == 'line':
        for _ in range(30):
            p_start = Point2D(random.randint(0, 255), random.randint(0, 255), drawer=drawer)
            p_end = Point2D(random.randint(0, 255), random.randint(0, 255), drawer=drawer)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            s.add(Line(p_start, p_end, drawer, color=Color(r, g, b)))
        s.draw()

    elif name_of_figure == 'circle':
        x = x_c
        y = y_c
        s.add(Circle(x, y, rad, drawer, color=Color(r, g, b)))
        for i in range(1, rad):
            a = int(sqrt(rad ** 2 - i ** 2))
            p_start = Point2D(x-a, y+i, drawer=drawer)
            p_end = Point2D(x+a, y+i, drawer=drawer)
            s.add(Line(p_start, p_end, drawer, color=Color(r, g, b)))
            p_start = Point2D(x-a, y-i, drawer=drawer)
            p_end = Point2D(x+a, y-i, drawer=drawer)
            s.add(Line(p_start, p_end, drawer, color=Color(r, g, b)))
        p_start = Point2D(x-rad, y, drawer=drawer)
        p_end = Point2D(x+rad, y, drawer=drawer)
        s.add(Line(p_start, p_end, drawer, color=Color(r, g, b)))
        s.draw()

    elif name_of_figure == 'square':
        x = x_c
        y = y_c
        p_start = Point2D(x, y, drawer=drawer)
        s.add(Square(p_start, w, h, drawer, color=Color(r, g, b)))
        for i in range(0, w+1):
            p_start = Point2D(x, y + i, drawer=drawer)
            p_end = Point2D(x+h, y+i, drawer=drawer)
            s.add(Line(p_start, p_end, drawer, color=Color(r, g, b)))
        s.draw()


if __name__ == '__main__':
    while True:

        drawer = Drawer(256, 256)

        name_of_file = input('Name of file (you can push file.txt as the link or exit): ')

        if name_of_file == 'exit':
            raise SystemExit()

        elif '\\' in name_of_file:
            with open(f'{name_of_file}', 'r') as open_f:
                name_of_file = name_of_file[:-4]
                lines = open_f.readlines()
                for i in range(0, len(lines)):
                    line = lines[i].lower().strip()
                    if line == 'line':
                        figure = 'line'
                        print(f'figure: {figure}')
                        main()

                    elif line == 'circle':
                        figure = 'circle'
                        print(f'figure: {figure}')
                        x_center, y_center = map(int, lines[i+1].split())
                        print(f'x_center: {x_center}, y_center: {y_center}')
                        radius = int(lines[i+2].strip())
                        print(f'radius: {radius}')
                        r_color, g_color, b_color = map(int, lines[i+3].split())
                        print(f'RGB: {r_color} {g_color} {b_color}')
                        main(name_of_figure=figure, x_c=x_center, y_c=y_center, rad=radius, r=r_color, g=g_color, b=b_color)

                    elif line == 'square':
                        figure = 'square'
                        print(f'figure: {figure}')
                        x0, y0 = map(int, lines[i+1].split())
                        print(f'x0, y0: {x0} {y0}')
                        w, h = map(int, lines[i+2].split())
                        print(f'width, height: {w} {h}')
                        r_color, g_color, b_color = map(int, lines[i+3].split())
                        print(f'RGB: {r_color} {g_color} {b_color}')
                        main(name_of_figure=figure, x_c=x0, y_c=y0, w=w, h=h, r=r_color, g=g_color, b=b_color)

        elif '\\' not in name_of_file:
            with open(f'{name_of_file}.txt', 'w') as open_f:
                while True:
                    figure = input('Line, circle or square? Responce or input "exit": ').lower()

                    if figure == 'circle':
                        open_f.write(f'{figure}\n')
                        x_center, y_center = map(int, input().split())
                        open_f.write(f'{x_center} {y_center}\n')
                        radius = int(input())
                        open_f.write(f'{radius}\n')
                        r_color, g_color, b_color = map(int, input().split())
                        open_f.write(f'{r_color} {g_color} {b_color}\n')
                        main(name_of_figure=figure, x_c=x_center, y_c=y_center,
                             rad=radius, r=r_color, g=g_color, b=b_color)

                    elif figure == 'square':
                        open_f.write(f'{figure}\n')
                        x0, y0 = map(int, input().split())
                        open_f.write(f'{x0} {y0}\n')
                        w, h = map(int, input().split())
                        open_f.write(f'{w} {h}\n')
                        r_color, g_color, b_color = map(int, input().split())
                        open_f.write(f'{r_color} {g_color} {b_color}\n')
                        main(name_of_figure=figure, x_c=x0, y_c=y0, w=w, h=h, r=r_color, g=g_color, b=b_color)

                    elif figure == 'line':
                        open_f.write(f'{figure}\n')
                        main()

                    elif figure == 'exit':
                        break

        drawer.save(name_of_file)
