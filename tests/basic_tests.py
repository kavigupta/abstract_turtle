
from math import pi

from collections import Counter

from abstract_turtle import Turtle, LoggingCanvas

from .utils import TestCase2

class BasicSquareTest(TestCase2):

    def setUp(self):
        self.canvas = LoggingCanvas(1000, 1000)
        self.turtle = Turtle(self.canvas)

    def assertPositionAlmostEqual(self, t, pos):
        self.assertContainersAlmostEqual(t.pos(), pos)

    def test_square(self):
        t = self.turtle
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
            {'draw_rectangular_line' : 4, 'refreshed_turtle' : 9},
            Counter([func for func, *_ in self.canvas.log])
        )
    def test_degrees(self):
        t = self.turtle
        t.rt(45)
        self.assertEqual(45, t.heading())
        t.degrees(400)
        self.assertAlmostEqual(50, t.heading())
        t.radians()
        self.assertAlmostEqual(pi/4, t.heading())

    def test_home(self):
        t = self.turtle
        t.rt(45)
        t.fd(100)
        t.home()
        self.assertAlmostEqual(0, t.heading())
        self.assertPositionAlmostEqual(t, (0, 0))

    def test_pensize(self):
        t = self.turtle
        self.assertEqual(1, t.pensize())
        t.pensize(10)
        self.assertEqual(10, t.pensize())

    def test_penupdown(self):
        t = self.turtle
        self.assertEqual(True, t.isdown())
        t.penup()
        self.assertEqual(False, t.isdown())

    def test_distance(self):
        t1 = self.turtle
        t1.setpos(3, 8)
        t2 = Turtle(LoggingCanvas(1000, 1000))
        t2.setpos(6, 12)

        self.assertAlmostEqual(t1.distance(t2), 5)
        self.assertAlmostEqual(t1.distance((0, 5)), 3 * 2**0.5)

    def test_bad_color_string(self):
        t1 = self.turtle
        try:
            t1.bgcolor('reds')
            self.fail()
        except RuntimeError as e:
            self.assertEqual(str(e), "Invalid color string: 'reds'")

    def test_bad_hex_color(self):
        t1 = self.turtle
        try:
            t1.bgcolor('#hello')
            self.fail()
        except RuntimeError as e:
            self.assertEqual(str(e), "Invalid hex color string: 'hello'")

    def test_bad_hex_color_parsing(self):
        t1 = self.turtle
        try:
            t1.bgcolor('#bcdefg')
            self.fail()
        except RuntimeError as e:
            self.assertEqual(str(e), "Invalid hex color string: 'bcdefg'")

    def test_bad_integer_color(self):
        t1 = self.turtle
        try:
            t1.bgcolor(0, 280, 30)
            self.fail()
        except RuntimeError as e:
            self.assertEqual(str(e), "Invalid integer color: (0, 280, 30)")

    def test_bad_types(self):
        t1 = self.turtle
        try:
            t1.bgcolor(0, 40.0, 30)
            self.fail()
        except RuntimeError as e:
            self.assertEqual(str(e), "Invalid color. Expected either 3 ints or 1 string, but got: int, float, int")
