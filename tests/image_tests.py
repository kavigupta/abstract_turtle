
import unittest

import numpy as np
from PIL import Image

from abstract_turtle import Turtle, PillowCanvas

# set this to true to create the images
REFRESH_IMAGES = False

class BasicSquareTest(unittest.TestCase):

    def setUp(self):
        self.canvas = PillowCanvas(1000, 1000)
        self.turtle = Turtle(self.canvas)

    def assertImageEquals(self, path):
        data = self.canvas.export()
        if REFRESH_IMAGES:
            data.save(path, "png")
        else:
            saved_data = np.array(Image.open(path).convert("RGBA"))
            self.assertTrue(np.array_equal(data, saved_data))

    def test_square(self):
        t = self.turtle
        for _ in range(36):
            for _ in range(4):
                t.fd(100)
                t.rt(90)
            t.rt(10)
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
        t.setheading(45)
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
