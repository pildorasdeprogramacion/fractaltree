import turtle
import random

def dibuja_arbol(longitud, diminucion , angulo, ruido=0):
    if longitud < 10:
        return
    turtle.width(longitud/12)
    turtle.forward(longitud)
    cambio_longitud = longitud*diminucion
    if ruido:
        cambio_longitud *= random.uniform(0.9,1.1) 

    angulo_derecho = angulo + random.gauss(0, ruido)
    angulo_izquierdo = angulo + random.gauss(0, ruido)
    
    turtle.left(angulo_izquierdo)
    dibuja_arbol(cambio_longitud,diminucion,angulo,ruido)
    turtle.right(angulo_izquierdo)

    
    turtle.right(angulo_derecho)
    dibuja_arbol(cambio_longitud,diminucion,angulo,ruido)
    turtle.left(angulo_derecho)

    turtle.backward(longitud)

turtle.bgcolor('black')
turtle.pencolor('white')
turtle.penup()
turtle.goto(0,-300)
turtle.pendown()
turtle.left(90)
turtle.speed(10)
dibuja_arbol(130,0.8,18,8)
turtle.done()
