from turtle import Turtle

sasuke = Turtle()
sasuke.shape("turtle")
sasuke.color("coral")

for _ in range(15):
    sasuke.forward(10)
    # .penup()  levantará a tartaruga da “tela digital” e se você mover a tartaruga no estado penup ela não desenhará
    sasuke.penup()
    sasuke.forward(10)
    #.pendown()  é o estado padrão de turtle. Isso garantirá que a tartaruga desenhe quando estiver se movendo com seus
    # comandos, como  forward()  ou  setpos().
    sasuke.pendown()