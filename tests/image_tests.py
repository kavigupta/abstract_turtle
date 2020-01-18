
import unittest

import numpy as np
from PIL import Image

from abstract_turtle import Turtle, PillowCanvas, ForwardingCanvas

# set this to true to create the images
REFRESH_IMAGES = False

class PillowTest(unittest.TestCase):

    def setUp(self, width=1000, height=1000):
        self.canvas = PillowCanvas(width, height)
        self.turtle = Turtle(self.canvas)

    def assertImageEquals(self, path, hide_turtle=True):
        if hide_turtle:
            self.turtle.hideturtle()
        data = self.canvas.export()
        if REFRESH_IMAGES:
            data.save(path, "png")
        else:
            saved_data = np.array(Image.open(path).convert("RGBA"))
            self.assertTrue(np.array_equal(data, saved_data))

    def test_square(self):
        t = self.turtle
        for _ in range(9):
            for _ in range(4):
                t.fd(100)
                t.rt(90)
            t.rt(40)
        self.assertImageEquals("test_img/squareflower.png")

    def test_centeredness(self):
        t = self.turtle
        t.setpos(0, 100)
        t.setpos(0, -100)
        t.setpos(0, 0)
        t.setpos(100, 0)
        t.setpos(-100, 0)
        t.setpos(0, 0)
        t.width(20)
        t.setpos(0, 0)
        t.rt(45)
        t.fd(100)
        self.assertImageEquals("test_img/centeredness.png")

    def test_multisegment_forward(self):
        t = self.turtle
        t.width(20)
        for _ in range(3):
            t.fd(100)
        self.assertImageEquals("test_img/multiseg_forward.png")

    def test_empty_star(self):
        t = self.turtle
        t.lt(18)
        for _ in range(5):
            t.fd(100)
            t.lt(180 - 36)
            t.fd(100)
            t.rt(72)
        self.assertImageEquals("test_img/empty_star.png")

    def test_full_star(self):
        t = self.turtle
        t.fillcolor(255, 0, 0)
        t.width(10)
        t.begin_fill()
        t.lt(18)
        for _ in range(5):
            t.fd(100)
            t.lt(180 - 36)
            t.fd(100)
            t.rt(72)
        t.end_fill()
        self.assertImageEquals("test_img/full_star.png")

    def test_circle(self):
        t = self.turtle
        t.fd(100)
        t.circle(100)
        t.fd(100)
        self.assertImageEquals("test_img/basic_circle.png")

    def test_thick_circle(self):
        t = self.turtle
        t.width(10)
        t.circle(100)
        t.fd(100)
        self.assertImageEquals("test_img/thick_circle.png")

    def test_background(self):
        t = self.turtle
        t.pencolor(255, 255, 255)
        t.fd(100)
        t.bgcolor(255, 255, 0)
        t.rt(90)
        t.fd(100)
        self.assertImageEquals("test_img/background_test.png")

    def test_multicolor(self):
        t = self.turtle
        t.pencolor(255, 255, 0)
        t.fd(100)
        t.pencolor(0, 255, 255)
        t.fd(100)
        t.pencolor(0, 255, 0)
        t.fd(100)
        self.assertImageEquals("test_img/multicolor.png")

    def test_multi_directions(self):
        t = self.turtle
        for _ in range(8):
            t.fd(20)
            t.pu()
            t.fd(10)
            t.pd()
            t.rt(45)
        self.assertImageEquals("test_img/multi_directions.png")

    def test_setvarious_things(self):
        t = self.turtle
        t.setx(100)
        t.sety(100)
        self.assertEqual((100, 100), t.pos())
        t.setx(0)
        t.sety(0)
        t.setheading(-45)
        t.fd(100)
        self.assertImageEquals("test_img/set_various_things.png")

    def test_dot(self):
        t = self.turtle
        t.width(50)
        t.dot()
        t.pencolor(0, 0, 255)
        t.dot(50)

        t.width(1)
        t.pencolor(255, 0, 0)
        t.fd(50)
        t.pencolor(0, 255, 0)
        t.fd(50)
        self.assertImageEquals("test_img/dot.png")

    def test_backward(self):
        t = self.turtle
        t.fd(100)
        t.rt(45)
        t.bk(100)
        self.assertImageEquals("test_img/bk.png")

    def test_clear(self):
        t = self.turtle
        t.fd(100)
        t.rt(45)
        t.bgcolor(255, 0, 0)
        t.clear()
        t.rt(90)
        t.fd(100)
        self.assertImageEquals("test_img/clear.png")

    def test_reset(self):
        t = self.turtle
        t.fd(100)
        t.rt(45)
        t.bgcolor(255, 0, 0)
        t.reset()
        t.rt(90)
        t.fd(100)
        self.assertImageEquals("test_img/reset.png")

    def test_color(self):
        t = self.turtle
        for _ in range(2):
            t.fd(100)
            for _ in range(4):
                t.fd(10)
                t.rt(90)
            t.fd(100)
            t.color(255, 0, 0)
        self.assertImageEquals("test_img/test_color.png")

    def test_turtle_drawn_correctly_at_start(self):
        self.assertImageEquals("test_img/just_turtle.png", hide_turtle=False)

    def test_turtle_at_pos(self):
        t = self.turtle
        t.fd(10)
        t.rt(45)
        t.fd(20)
        self.assertImageEquals("test_img/turtle_at_pos.png", hide_turtle=False)

    def test_turtle_full_rotate(self):
        t = self.turtle
        t.fd(10)
        t.rt(45 + 360)
        t.fd(20)
        self.assertImageEquals("test_img/turtle_full_rotate.png", hide_turtle=False)

    def test_color_strings(self):
        t = self.turtle
        t.pencolor("#12fa0b")
        t.fd(100)
        t.pencolor("red")
        t.fd(100)
        t.pencolor("#1fb")
        t.fd(100)
        self.assertImageEquals("test_img/color_strings.png")

    def test_partial_circle(self):
        t = self.turtle
        t.fd(100)
        t.circle(100, 90)
        t.fd(100)
        t.circle(50, -90)
        t.fd(100)
        t.circle(-50, 90)
        t.fd(100)
        t.circle(-50, -90)
        t.fd(100)
        self.assertImageEquals("test_img/partial_circle.png")

    def test_partial_circle_fill(self):
        t = self.turtle
        t.begin_fill()
        t.fillcolor("red")
        t.fd(100)
        t.circle(100, 90)
        t.fd(100)
        t.end_fill()
        self.assertImageEquals("test_img/partial_circle_fill.png")

    def test_simple_partial_circle(self):
        t = self.turtle
        t.fd(100)
        t.circle(100, 90)
        t.fd(100)
        self.assertImageEquals("test_img/simple_partial_circle.png")

    def test_pixel(self):
        t = self.turtle
        t.pixel_size(100)
        t.pixel(0, 0, "red")
        t.pixel_size(50)
        t.pixel(1.5, 0.5, "green")
        self.assertImageEquals("test_img/test_pixel.png")

    def test_1x1_pixel(self):
        self.setUp(10, 10)
        t = self.turtle
        t.pixel(0, 0, "black")
        t.pixel(1, 0, "red")
        t.pixel(1, 1, "green")
        t.pixel(0, 1, "blue")
        t.pixel(-1, 1, "yellow")
        t.pixel(-1, 0, "magenta")
        t.pixel(-1, -1, "cyan")
        t.pixel(0, -1, "orange")
        t.pixel(1, -1, "purple")
        self.assertImageEquals("test_img/test_1x1_pixel.png")

    def test_standard_mode(self):
        t = self.turtle
        t.fd(100)  # should move to the east
        t.lt(90)  # should face north
        t.fd(100)  # should move north
        t.setheading(-90)  # should face south
        t.fd(200)  # should move south
        self.assertImageEquals("test_img/test_standard_mode.png")

    def test_logo_mode(self):
        t = self.turtle
        t.mode("logo")
        t.fd(100)  # should move to the north
        t.lt(90)  # should face west
        t.fd(100)  # should move west
        t.setheading(-90)  # should stay facing west
        t.fd(200)  # should move west
        self.assertImageEquals("test_img/test_logo_mode.png")

class ForwardingTest(PillowTest):
    def setUp(self, width=1000, height=1000):
        self.underlying_canvas = PillowCanvas(width, height)
        self.canvas = ForwardingCanvas(self.underlying_canvas)
        self.turtle = Turtle(self.canvas)

    def assertImageEquals(self, path, hide_turtle=True):
        if hide_turtle:
            self.turtle.hideturtle()
        data = self.underlying_canvas.export()
        saved_data = np.array(Image.open(path).convert("RGBA"))
        self.assertTrue(np.array_equal(data, saved_data))
