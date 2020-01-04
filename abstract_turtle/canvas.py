
from abc import ABC, abstractmethod

class Canvas(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def draw_rectangular_line(self, start, end, color, width):
        """
        Draw a 1 width line from START to END with the given color COLOR
        """
        pass

    def draw_line(self, start, end, color, width):
        if width > 1:
            self.draw_circle(start, width / 2, color, width, True)
        self.draw_rectangular_line(start, end, color, width)
        if width > 1:
            self.draw_circle(end, width / 2, color, width, True)

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

    @abstractmethod
    def update_turtle(self, drawn_turtle):
        """
        Update the turtle to the given DrawnTurtle object, or remove the turtle if None is passed
        """
        pass

    @abstractmethod
    def last_turtle(self):
        """
        Get the last DrawnTurtle object provided to this canvas.
        """
        pass
