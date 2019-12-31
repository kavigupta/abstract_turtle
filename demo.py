
from abstract_turtle.turtle import Turtle
from abstract_turtle.pillow_canvas import PillowCanvas

import matplotlib.pyplot as plt

c = PillowCanvas(1000, 1000)
t = Turtle(c)

for _ in range(4):
    t.fd(100)
    print(t.pos())
    t.rt(90)

image = c.export()
plt.imsave('square.png', image)
