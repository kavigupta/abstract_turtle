
from .canvas import Canvas

class LoggingCanvas(Canvas):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.log = []

    def draw_rectangular_line(self, start, end, color, width):
        self.log.append(['draw_rectangular_line', [start.x, start.y, end.x, end.y], color, width])

    def draw_circle(self, center, radius, color, width, is_filled):
        self.log.append(['draw_circle', [center.x, center.y, radius], color, width, is_filled])

    def fill_polygon(self, points, color):
        self.log.append(['fill_polygon', [[point.x, point.y] for point in points], color])

    def set_bgcolor(self, color):
        self.log.append(['set_bgcolor', color])

    def clear(self):
        self.log.append(['clear'])
