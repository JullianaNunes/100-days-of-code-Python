# 2. Move the snake

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") # Define cor da tela
screen.title("Jogo da cobrinha!")
screen.tracer(0) # Turn turtle animation on/off and set delay for update drawings

starting_positions = [(0,0), (-20,0), (-40,0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)



game_is_on = True

while game_is_on:
    screen.update()  # Perform a TurtleScreen update. To be used when tracer is turned off.
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)



screen.exitonclick()
# Documentação https://docs.python.org/3.1/library/turtle.html