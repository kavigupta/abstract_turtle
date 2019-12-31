
from abc import ABC, abstractmethod

class Canvas(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def draw_line(self, start, end, color, width):
        """
        Draw a 1 width line from START to END with the given color COLOR
        """
        pass

    @abstractmethod
    def draw_circle(self, center, radius, color, width, is_filled):
        """
        Draw a circle of width 1 with the given center CENTER, radius RADIUS, and color COLOR

        Fill the circle if IS_FILLED is true.
        """
        pass

    @abstractmethod
    def fill_polygon(self, points, color):
        """
        Fill the given polygon with edge points POINTS and fill color COLOR.
        """
        pass

    @abstractmethod
    def set_bgcolor(self, color):
        """
        Fill the entire background with the given COLOR
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Clear everything in the foreground
        """
        pass
