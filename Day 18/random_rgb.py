''' Documentação
- https://en.wikipedia.org/wiki/Random_walk
'''

import turtle
import random

zen = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
zen.pensize(15)
zen.speed("fastest")

for _ in range(200):
    zen.color(random_color())
    zen.forward(30)
    zen.setheading(random.choice(directions))

