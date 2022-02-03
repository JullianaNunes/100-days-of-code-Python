from turtle import Turtle
import random

hima = Turtle()

cores = ["MediumOrchid", "Orchid", "Plum", "Thistle", "MediumOrchid", "Orchid", "Plum", "Thistle"]

def shape(num):
    ang = 360 / num
    for _ in range(num):
        hima.forward(100)
        hima.right(ang)

for formato in range(3, 10):
    hima.color(random.choice(cores))
    shape(formato)