from turtle import Turtle, Screen

jade = Turtle()
screen = Screen()

def em_frente():
    jade.forward(10)

def para_tras():
    jade.backward(10)

def esquerda():
    # heading = Retorna o título atual da tartaruga (o valor depende do modo da tartaruga, veja mode()).
    novo_heading = jade.heading() + 10
    jade.setheading(novo_heading)

def direita():
    novo_heading = jade.heading() - 10
    jade.setheading(novo_heading)

def limpa():
    jade.clear()
    jade.penup()
    jade.home()
    jade.pendown()

screen.listen()
screen.onkey(em_frente, "Up")
screen.onkey(para_tras(), "Down")
screen.onkey(esquerda(), "Left")
screen.onkey(direita(), "Right")
screen.onkey(limpa, "c")

screen.exitonclick()