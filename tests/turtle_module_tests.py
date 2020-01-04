
import unittest

from collections import Counter

from abstract_turtle import LoggingCanvas
from abstract_turtle.turtle import *

class TestTurtleModule(unittest.TestCase):

    def test_module_import_star(self):
        canvas = LoggingCanvas(1000, 1000)
        set_canvas(canvas)
        fd(100)
        rt(90)
        self.assertAlmostEqual(0, xcor())
        self.assertAlmostEqual(100, ycor())
        self.assertAlmostEqual(90, heading())
        self.assertEqual(
            {'draw_rectangular_line' : 1, 'update_turtle' : 3},
            Counter([func for func, *_ in canvas.log])
        )
