
import unittest

import numpy as np
import matplotlib.pyplot as plt

from abstract_turtle.turtle import Turtle
from abstract_turtle.pillow_canvas import PillowCanvas

# set this to true to create the images
REFRESH_IMAGES = True

class BasicSquareTest(unittest.TestCase):

    def setUp(self):
        self.canvas = PillowCanvas(1000, 1000)
        self.turtle = Turtle(self.canvas)

    def assertImageEquals(self, path):
        data = self.canvas.export().astype(np.float32) / 255
        if REFRESH_IMAGES:
            plt.imsave(path, data)
        else:
            saved_data = plt.imread(path)
            self.assertTrue(np.array_equal(data, saved_data))

    def test_square(self):
        t = self.turtle
        for _ in range(36):
            for _ in range(4):
                t.fd(100)
                t.rt(90)
            t.rt(10)
        self.assertImageEquals("img/squareflower.png")

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
        self.assertImageEquals("img/centeredness.png")

    def test_multisegment_forward(self):
        t = self.turtle
        t.width(20)
        for _ in range(3):
            t.fd(100)
        self.assertImageEquals("img/multiseg_forward.png")

    def test_empty_star(self):
        t = self.turtle
        t.lt(18)
        for _ in range(5):
            t.fd(100)
            t.lt(180 - 36)
            t.fd(100)
            t.rt(72)
        self.assertImageEquals("img/empty_star.png")

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
        self.assertImageEquals("img/full_star.png")

    def test_circle(self):
        t = self.turtle
        t.circle(100)
        t.fd(100)
        self.assertImageEquals("img/basic_circle.png")

    def test_thick_circle(self):
        t = self.turtle
        t.width(10)
        t.circle(100)
        t.fd(100)
        self.assertImageEquals("img/thick_circle.png")

    def test_background(self):
        t = self.turtle
        t.pencolor(255, 255, 255)
        t.fd(100)
        t.bgcolor(255, 255, 0)
        t.rt(90)
        t.fd(100)
        self.assertImageEquals("img/background_test.png")

    def test_multicolor(self):
        t = self.turtle
        t.pencolor(255, 255, 0)
        t.fd(100)
        t.pencolor(0, 255, 255)
        t.fd(100)
        t.pencolor(0, 255, 0)
        t.fd(100)
        self.assertImageEquals("img/multicolor.png")
