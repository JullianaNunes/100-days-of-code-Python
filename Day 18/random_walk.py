from turtle import Turtle
import random

sasuke = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
sasuke.pensize(15)
sasuke.speed("fastest")

for _ in range(200):
    sasuke.color(random.choice(colours))
    sasuke.forward(30)
    sasuke.setheading(random.choice(directions))

