
from collections import namedtuple

from math import sin, cos

from .color_names import COLORS


class Color(namedtuple('Color', ['red', 'green', 'blue'])):
    @staticmethod
    def of(*color):
        if len(color) == 3:
            if any(not isinstance(c, int) for c in color):
                raise RuntimeError("Not a valid color: %s" % color)
            return Color(*color)
        if len(color) == 1 and isinstance(color[0], str):
            color = color[0].lower()
            if color and color[0] == "#":
                if len(color) == 4:  # shorthand hex
                    color = "".join(x * 2 for x in color)[1:]
                if len(color) == 7:
                    digits = color[1:]
                    vals = [Color.hexparse(digits[i:i+2]) for i in range(0, 6, 2)]
                    return Color.of(*vals)
                raise RuntimeError("Invalid hex color string")
            if color in COLORS:
                return Color.of(COLORS[color])
            raise RuntimeError("Invalid color string")
        raise RuntimeError("Invalid color")

    @staticmethod
    def hexparse(pair):
        try:
            return int(pair, 16)
        except ValueError:
            raise RuntimeError("Invalid hex color string")


Position = namedtuple('Position', ['x', 'y'])

class DrawnTurtle(namedtuple('DrawnTurtle', ['pos', 'heading', 'stretch_wid', 'stretch_len'])):
    @property
    def points(self):
        unadjusted_points = [
            (-3, 8),
            (0, 0),
            (-3, -8),
            (8, 0),
        ]
        stretched_points = [
            (dx * self.stretch_len, dy * self.stretch_wid) for dx, dy in unadjusted_points
        ]
        rotated_points = [
            rotate(*dxy, self.heading) for dxy in stretched_points
        ]
        moved_points = [
            Position(self.pos.x + dx, self.pos.y + dy) for dx, dy in rotated_points
        ]
        return moved_points

    @property
    def json_friendly(self):
        return [
            [self.pos.x, self.pos.y],
            self.heading,
            self.stretch_wid,
            self.stretch_len
        ]

def rotate(x, y, theta):
    return x * cos(theta) - y * sin(theta), x * sin(theta) + y * cos(theta)
