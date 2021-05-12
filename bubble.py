#Javier Alejadnro Mazariegos Godoy
#20200223
import random
import turtle
import time
from tkinter import *
listado = []
wn = turtle.Screen()
wn.title("Bubble sort")
print(wn.screensize())
class cuadrados(turtle.Turtle):
    def __init__(self, data, pointx):
        turtle.Turtle.__init__(self)
        self.penup()
        self.data = data
        self.shape("square")
        self.shapesize(data*0.1,1)
        self.color("gray")
        self.pointx = pointx
        self.pointy = 0
        self.setx(pointx)
        self.sety(data)

class escribir(turtle.Turtle):
    def __init__(self, data, pointx, pointy):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.setx(pointx)
        self.sety(pointy)
        self.write(data)

class cuadraditos(turtle.Turtle):
    def __init__(self, pointx, pointy):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.shapesize(1,1)
        self.setx(pointx)
        self.sety(pointy)
        
class botones(turtle.Turtle):
    def __init__(self, data, pointx, pointy):
        turtle.Turtle.__init__(self)
        self.penup()
        self.data = data
        self.shape("triangle")
        self.shapesize(3,3)
        self.color("green")
        self.setx(pointx)
        self.sety(pointy)


def numero_random(numero):
    global listado
    numero_datos = int(numero/2)
    residuo = 0
    pointx = 0
    for i in range(numero):
        residuo = (numero_datos - (i))*-1
        pointx = residuo * (wn.screensize()[0]/numero_datos)
        listado.append(cuadrados(random.randint(1,(wn.screensize()[1]/2)-10), pointx))
    
def bubbleSort(x,y):
    global listado,wn
    n = len(listado)
 
    for i in range(n):
        for j in range(0, n-i-1):
            listado[j].color("green")
            listado[j+1].color("red")
            if listado[j].data > listado[j+1].data :
                temp = listado[j].pointx
                temp_objeto = listado[j]
                time.sleep(1)
                listado[j].setx(listado[j+1].pointx)
                listado[j].pointx =listado[j+1].pointx
                listado[j] = listado[j+1]
                time.sleep(1)
                listado[j+1].setx(temp)
                listado[j+1].pointx = temp
                listado[j+1] = temp_objeto
            else:
                time.sleep(1)
                pass
            listado[j].color("gray")
            listado[j+1].color("gray")
    messagebox.showinfo("Buublesort","Termino!")


numero_de_cuadros = int(turtle.textinput("Cuadros", "Cauntos numeros aleatorios desea genrar?"))
cuadrado1 = cuadraditos((wn.screensize()[0]*-1)-60, (wn.screensize()[1])+80)
cuadrado1.color("green")
texto1 = escribir("Numero actual",(wn.screensize()[0]*-1)-45, (wn.screensize()[1])+67)
cuadrado2 = cuadraditos((wn.screensize()[0]*-1)-60, (wn.screensize()[1])+50)
cuadrado2.color("red")
texto2 = escribir("Numero de comparacion",(wn.screensize()[0]*-1)-45, (wn.screensize()[1])+37)
numero_random(numero_de_cuadros)

boton1 = botones("Bubblesort",0,-100)
boton1.onclick(bubbleSort)


while True:
    wn.update()
wn.mainloop()
