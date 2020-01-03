
from collections import namedtuple

def cons_color(*color):
    if len(color) == 3:
        if any(not isinstance(c, int) for c in color):
            raise RuntimeError("Not a valid color: %s" % color)
        return Color(*color)
    raise RuntimeError("String colors not supported")


Color = namedtuple('Color', ['red', 'green', 'blue'])
Color.of = cons_color

Position = namedtuple('Position', ['x', 'y'])
