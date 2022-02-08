''' Documentação
- https://en.wikipedia.org/wiki/Random_walk
'''

from turtle import Turtle
import random

zen = Turtle()

colours = ["MediumOrchid", "Orchid", "Plum", "Thistle", "MediumOrchid", "Orchid", "Plum", "Thistle"]
directions = [0, 90, 180, 270]
zen.pensize(15)
zen.speed("fastest")

for _ in range(200):
    zen.color(random.choice(colours))
    zen.forward(30)
    zen.setheading(random.choice(directions))