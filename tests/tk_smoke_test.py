
from time import sleep
import unittest

from abstract_turtle import Turtle
from abstract_turtle.tk_canvas import TkCanvas
from .image_tests import PillowTest

MANUAL_INSPECT = False

class TkSmokeTest(PillowTest):
    def setUp(self, width=1000, height=1000):
        self.canvas = TkCanvas(width, height)
        self.turtle = Turtle(self.canvas)
        self.turtle.clear()
        self.turtle.bgcolor("white")
        if not MANUAL_INSPECT:
            import turtle
            turtle.speed(0)

    def assertImageEquals(self, path, hide_turtle=True):
        if MANUAL_INSPECT:
             # give a second to inspect the image
            sleep(1)

del PillowTest
