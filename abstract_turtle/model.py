
import attr

@attr.s
class Color:
    red = attr.ib()
    green = attr.ib()
    blue = attr.ib()
    def of(self, *color):
        if len(color) == 3:
            if any(not isinstance(c, int) for c in color):
                raise RuntimeError("Not a valid color: %s" % color)
            return Color(*color)
        raise RuntimeError("String colors not supported")

@attr.s
class Position:
    x = attr.ib()
    y = attr.ib()
