import turtle
import random

zen = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        zen.color(random_color())
        # Tamanho do círculo
        zen.circle(100)
        zen.setheading(zen.heading() + size_of_gap)

zen.speed("fastest")
draw_spirograph(5)
screen = turtle.Screen()
screen.exitonclick()


