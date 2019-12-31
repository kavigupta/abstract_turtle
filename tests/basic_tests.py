
import unittest

from collections import Counter

from abstract_turtle.turtle import Turtle
from abstract_turtle.logging_canvas import LoggingCanvas

class BasicSquareTest(unittest.TestCase):

    def assertPositionAlmostEqual(self, t, pos):
        self.assertAlmostEqual(t.xcor(), pos[0])
        self.assertAlmostEqual(t.ycor(), pos[1])

    def test_square(self):
        canvas = LoggingCanvas(1000, 1000)
        t = Turtle(canvas)
        self.assertPositionAlmostEqual(t, (0, 0))
        t.fd(100)
        t.rt(90)
        self.assertPositionAlmostEqual(t, (0, 100))
        t.fd(100)
        t.rt(90)
        self.assertPositionAlmostEqual(t, (100, 100))
        t.fd(100)
        t.rt(90)
        self.assertPositionAlmostEqual(t, (100, 0))
        t.fd(100)
        t.rt(90)
        self.assertPositionAlmostEqual(t, (0, 0))

        self.assertEqual(
            {'draw_rectangular_line' : 4, 'draw_circle' : 8},
            Counter([func for func, *_ in canvas.log])
        )
