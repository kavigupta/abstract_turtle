
from time import sleep
import unittest

from abstract_turtle import Turtle
from abstract_turtle.tk_canvas import TkCanvas
from .image_tests import PillowTest

# unfortunately this can't run in headless mode. Delete this line to visually inspect the results
@unittest.skip
class TkSmokeTest(PillowTest):
    def setUp(self, width=1000, height=1000):
        self.canvas = TkCanvas(width, height)
        self.turtle = Turtle(self.canvas)
        self.turtle.clear()
        self.turtle.bgcolor("white")
        import turtle

    def assertImageEquals(self, path, hide_turtle=True):
        sleep(1) # give a second to inspect the image

del PillowTest
