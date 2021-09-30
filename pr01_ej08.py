from turtle import *
from math import sqrt
pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)
tortuga = Turtle()

l= float(input('Dime un valor para el lado del triangulo: '))
h = sqrt(3)/2*l

tortuga.penup()
tortuga.goto(-l/2,0)
tortuga.pendown()
tortuga.forward(l)
tortuga.goto(0,h)
tortuga.goto(-l/2,0)
tortuga.penup()
tortuga.goto(-l//2-1,-20)
tortuga.write("La altura del triangulo es: {0}".format(round(h,2)))
