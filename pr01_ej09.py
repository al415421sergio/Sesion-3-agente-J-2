from turtle import *
from math import sqrt
pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)
tortuga = Turtle()

l= float(input('Dime un valor para el lado del triangulo: '))
h = sqrt(3)/2*l
centroide_x = (-l/2+l/2+0)/3
centroide_y = (0+0+h)/3

tortuga.penup()
tortuga.goto(-l/2,0)
tortuga.pendown()
tortuga.forward(l)
tortuga.goto(0,h)
tortuga.goto(-l/2,0)
tortuga.penup()
tortuga.goto(centroide_x,centroide_y)
tortuga.dot()
tortuga.write('({0},{1})'.format(round(centroide_x,2),round(centroide_y,2)))
