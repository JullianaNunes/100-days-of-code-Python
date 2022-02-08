import turtle
from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
# screen.setup(500, 400) # Define a largura e altura da tela (nessa ordem)
screen.setup(width=500, height=400) # Outro jeito de usar
aposta = screen.textinput(title="Faça sua aposta", prompt="Qual tartaruga vai ganhar a corrida? Escolha uma cor:")

cores = ["red", "orange", "yellow", "green", "blue", "purple"]
lista_y = [-70, -40, -10, 20, 50, 80]
tartarugas = []

for t in range(0, 6):
    tartaruga = Turtle(shape="turtle")
    tartaruga.penup()
    tartaruga.color(cores[t])
    tartaruga.goto(x=-230, y=lista_y[t]) # Define coordenadas
    tartarugas.append(tartaruga)

if aposta:
    race_on = True

while race_on:
    for t in tartarugas:
        if t.xcor() > 230:
            race_on = False
            vencedor = t.pencolor()
            if vencedor == aposta:
                print(f"Você venceu uhul! A tartaruga {vencedor} ganhou!")
            else:
                print(f"Você perdeu :( A tartaruga {vencedor} ganhou!")

        distancia = random.randint(0,10)
        t.forward(distancia)

screen.exitonclick()

# Documentação - https://docs.python.org/3.1/library/turtle.html#turtle.textinput