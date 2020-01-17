
from math import sin, cos, pi, atan2
try:
    import turtle
    import tkinter
except ImportError:
    pass

from .canvas import Canvas
from .model import Color, Position, Arc


class TkCanvas(Canvas):
    """
    Draw the given results on a pillow canvas.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        self.image = None
        turtle.colormode(255)
        # TODO add init hook

    def tr_pos(self, pos):
        x, y = pos.x, pos.y
        return round(x), round(-y)

    @staticmethod
    def tr_color(color):
        return '#%02x%02x%02x' % tuple(color)

    def _goto(self, pos):
        turtle.goto(*pos)

    def _goto_invisible(self, pos):
        speed = turtle.speed()
        turtle.speed(0)
        turtle.pu()
        self._goto(pos)
        turtle.pd()
        turtle.speed(speed)

    def _goto_visible(self, pos, color, width):
        turtle.color(self.tr_color(color))
        turtle.width(width)
        self._goto(pos)

    def _setheading(self, heading):
        turtle.radians()
        turtle.setheading(heading)

    def draw_rectangular_line(self, start, end, color, width):
        self._goto_invisible(start)
        self._goto_visible(end, color, width)

    def draw_circle(self, center, radius, color, width, is_filled, start, end):
        if is_filled:
            assert start == 0
            assert end == 2 * pi
            x, y = self.tr_pos(center)
            left_up = (x-radius, y-radius)
            right_down = (x+radius, y+radius)
            box = [left_up, right_down]
            turtle.getcanvas().create_oval(box, fill=self.tr_color(color), width=0)
        else:
            arc_to_draw = Arc(center, radius, start, end)
            points = list(arc_to_draw.to_points())
            self._goto_invisible(points[0])
            for (px, py), (x, y) in zip(points, points[1:]):
                self._setheading(atan2(y - py, x - px))
                self._goto_visible((x, y), color, width)


    def fill_path(self, path, color):
        points = []
        for movement in path:
            points += movement.to_points()
        polygon = [coor for point in points for coor in self.tr_pos(point)]
        turtle.getcanvas().create_polygon(polygon,
            fill=self.tr_color(color))
        turtle.getcanvas().update_idletasks()

    def axis_aligned_rectangle(self, bottom_left, width, height, color):
        x, y = bottom_left
        blx, bly = self.tr_pos(bottom_left)
        # bounding box in pixel space, make this exactly w*h
        # subtract one to have blx, blx+1, ..., blx+w-1, etc.
        tlx, tly = blx + (width - 1), bly - (height - 1)
        turtle.getcanvas().create_rectangle(blx, bly, tlx, tly, fill=self.tr_color(color), width=0)

    def set_bgcolor(self, color):
        turtle.bgcolor(self.tr_color(color))

    def clear(self):
        self.axis_aligned_rectangle(Position(-self.width / 2, -self.height / 2), self.width, self.height, Color(255, 255, 255))
        turtle.clear()

    def refreshed_turtle(self, drawn_turtle):
        self._setheading(drawn_turtle.heading)
        self._goto_invisible(drawn_turtle.pos)
        turtle.shapesize(drawn_turtle.stretch_wid, drawn_turtle.stretch_len)
