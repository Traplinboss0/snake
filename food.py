#se importaron las librerias pertinentes al trabajo
from turtle import Turtle
import random


#se crea la clase food
class Food(Turtle):

#iniciamos funciones
    def __init__(self):
        #iniciamos funcion super
        super().__init__()
        #forma de la comida
        self.shape("circle")
        #evitamos que se genere lineas de recorrido
        self.penup()
        #Tamaño de la comida
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        #color de la comida
        self.color("red")
        #velocidad de la comida
        self.speed("fastest")
        #recarga la comida
        self.refresh()
    #funcion para refrescar
    def refresh(self):
        #asigna una pocision ramndon a la comida
        random_x = random.randint(-280, 280)
        #asigna una pocision ramndon a la comida
        random_y = random.randint(-280, 280)
        #lleva la comida a la pantalla
        self.goto(random_x, random_y)