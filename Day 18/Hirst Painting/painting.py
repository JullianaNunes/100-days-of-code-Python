import turtle
import random

lista_cores = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127,
195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]

turtle.colormode(255)
num_pontos = 100

mitsuki = turtle.Turtle()
mitsuki.shape("circle")
mitsuki.speed("fastest")
# .penup()  levantará a tartaruga da “tela digital” e se você mover a tartaruga no estado penup ela não desenhará
mitsuki.penup()
# Make the turtle invisible.
mitsuki.hideturtle()
mitsuki.setheading(225)
mitsuki.forward(300)
mitsuki.setheading(0)

for ponto in range(1, num_pontos + 1):
    mitsuki.dot(20, random.choice(lista_cores))
    mitsuki.forward(50)

    if ponto % 10 == 0:
        mitsuki.setheading(90)
        mitsuki.forward(50)
        mitsuki.setheading(180)
        mitsuki.forward(500)
        mitsuki.setheading(0)


screen = turtle.Screen()
screen.exitonclick()