from turtle import Turtle, Screen

tata = Turtle()
# Determina o formato
tata.shape("turtle")
# Determina a cor
tata.color("DarkSlateBlue")
# Determina a distância
tata.forward(100)

# Biblioteca para tela que a tartaruga irá aparecer
my_screen = Screen()
my_screen.canvheight

# Permitirá que o nosso programa continue a funcionar até clicarmos na tela.
my_screen.exitonclick()


# Documentação https://docs.python.org/3/library/turtle.html