
import unittest

import numpy as np
import matplotlib.pyplot as plt

from abstract_turtle.turtle import Turtle
from abstract_turtle.pillow_canvas import PillowCanvas

# set this to true to create the images
REFRESH_IMAGES = False

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

    def test_empty_star(self):
        t = self.turtle
        t.lt(18)
        for _ in range(5):
            t.fd(100)
            t.lt(180 - 36)
            t.fd(100)
            t.rt(72)
        self.assertImageEquals("img/empty_star.png")
