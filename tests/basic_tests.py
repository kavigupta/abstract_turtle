
from math import pi

from collections import Counter

from abstract_turtle import Turtle, LoggingCanvas, ForwardingCanvas

from .utils import TestCase2

class BasicSquareTest(TestCase2):

    def setUp(self, width=1000, height=1000):
        self.canvas = LoggingCanvas(width, height)
        self.turtle = Turtle(self.canvas)

    def assertPositionAlmostEqual(self, t, pos):
        self.assertContainersAlmostEqual(t.pos(), pos)

    def test_square(self):
        t = self.turtle
        self.assertPositionAlmostEqual(t, (0, 0))
        t.fd(100)
        t.rt(90)
        self.assertPositionAlmostEqual(t, (100, 0))
        t.fd(100)
        t.rt(90)
        self.assertPositionAlmostEqual(t, (100, -100))
        t.fd(100)
        t.rt(90)
        self.assertPositionAlmostEqual(t, (0, -100))
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
        self.assertEqual(360-45, t.heading())
        t.degrees(400)
        self.assertAlmostEqual(400-50, t.heading())
        t.radians()
        self.assertAlmostEqual(2*pi - pi/4, t.heading())

    def test_set_heading(self):
        t = self.turtle
        t.setheading(45)
        self.assertEqual(45, t.heading())

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

    def test_full_circle(self):
        t = self.turtle
        t.circle(2)
        self.assertContainersAlmostEqual(
            self.canvas.log,
            [
                ['refreshed_turtle', [[0, 0], 0, 1, 1]],
                ['draw_circle', [0, 2, 2], [0, 0, 0], 1, False, -pi/2, 3*pi/2],
                ['refreshed_turtle', [[0, 0], 0, 1, 1]],
            ]
        )

    def test_part_circle(self):
        t = self.turtle
        t.circle(2, 45)
        self.assertContainersAlmostEqual(
            self.canvas.log,
            [
                ['refreshed_turtle', [[0, 0], 0, 1, 1]],
                ['draw_circle', [0, 2, 2], [0, 0, 0], 1, False, -pi/2, -pi/4],
                ['refreshed_turtle', [[2**0.5, 2 - 2**0.5], pi/4, 1, 1]],
            ]
        )

    def test_rotated_full_circle(self):
        t = self.turtle
        t.lt(45)
        t.circle(2, 45)
        self.assertContainersAlmostEqual(
            self.canvas.log,
            [
                ['refreshed_turtle', [[0, 0], 0, 1, 1]],
                ['refreshed_turtle', [[0, 0], pi/4, 1, 1]],
                ['draw_circle', [-2**0.5, 2**0.5, 2], [0, 0, 0], 1, False, -pi/4, 0],
                ['refreshed_turtle', [[2 - 2**0.5, 2**0.5], pi/2, 1, 1]],
            ]
        )

    def test_partial_circle_fill(self):
        t = self.turtle
        t.pu()
        t.begin_fill()
        t.fillcolor("red")
        t.fd(100)
        t.circle(100, 90)
        t.fd(100)
        t.end_fill()
        self.assertContainersAlmostEqual(
            self.canvas.log,
            [
                ['refreshed_turtle', [[0, 0],       0, 1, 1]],
                ['refreshed_turtle', [[100, 0],     0, 1, 1]],
                ['refreshed_turtle', [[200, 100],  pi/2, 1, 1]],
                ['refreshed_turtle', [[200, 200],  pi/2, 1, 1]],
                ['fill_path', [
                        ['line', [0, 0]],
                        ['line', [100, 0]],
                        ['arc', [100, 100], 100, -pi / 2, 0],
                        ['line', [200, 200]]
                    ],
                    [255, 0, 0]
                ]
            ]
        )

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

    def test_mode(self):
        t = self.turtle
        t.mode("standard")
        self.assertEqual(t.mode(), "standard")
        t.mode("logo")
        self.assertEqual(t.mode(), "logo")

    def test_width_height_default(self):
        t = self.turtle
        self.assertEqual(t.canvas_width(), 1000)
        self.assertEqual(t.canvas_height(), 1000)
        t.pixel_size(2)
        self.assertEqual(t.canvas_width(), 500)
        self.assertEqual(t.canvas_height(), 500)
        t.pixel_size(3)
        self.assertEqual(t.canvas_width(), 333)
        self.assertEqual(t.canvas_height(), 333)

    def test_width_height_diff_sizes(self):
        self.setUp(200, 500)
        t = self.turtle
        self.assertEqual(t.canvas_width(), 200)
        self.assertEqual(t.canvas_height(), 500)
        t.pixel_size(2)
        self.assertEqual(t.canvas_width(), 100)
        self.assertEqual(t.canvas_height(), 250)
        t.pixel_size(3)
        self.assertEqual(t.canvas_width(), 66)
        self.assertEqual(t.canvas_height(), 166)

    def test_width_height_forwarding_canvas(self):
        c = ForwardingCanvas(LoggingCanvas(100, 200))
        t = Turtle(c)
        self.assertEqual(t.canvas_width(), 100)
        self.assertEqual(t.canvas_height(), 200)
        t.pixel_size(2)
        self.assertEqual(t.canvas_width(), 50)
        self.assertEqual(t.canvas_height(), 100)
        c.set_canvas(LoggingCanvas(2, 3))
        self.assertEqual(t.canvas_width(), 1)
        self.assertEqual(t.canvas_height(), 1)
