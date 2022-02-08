from turtle import Turtle, Screen

jade = Turtle()
screen = Screen()

def move_forwards():
    jade.forward(10)

screen.listen()
screen.onkey(key="space", fun = move_forwards)
screen.exitonclick()











# Documentação - https://docs.python.org/3/library/turtle.html#turtle.listen