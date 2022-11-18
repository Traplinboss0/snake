#importamos las librerias pertinentes para el proyrcto
from turtle import Turtle
#centramos el barra de puntaje
ALIGNMENT = "center"
#asignamos una fuente a la barra de puntaje
FONT = ("Courier", 24, "normal")

#Hacemos la clase correspondiente a la barra de puntaje
class Scoreboard(Turtle):
    #iniciamos lña funcion
    def __init__(self):
        #iniciamos la funcion super
        super().__init__()
        #asignamos un puntaje
        self.score = 0
        #asignamos un color al puntaje
        self.color("white")
        #evitamnos que genere lineas
        self.penup()
        #le asignamos una puntuacion a la barra de puntaje
        self.goto(0, 270)
        #ocultamos el contenido dentro de la barra dejando solo el texto
        self.hideturtle()
        #actualizamos la barra de puntaje
        self.update_scoreboard()

#le da forma y color a la fuente
    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)


#Actualiza la informacion de la barra de puntaje y muestra game over
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align=ALIGNMENT, font=FONT)

#se encarga de incrementar el púntaje conforme la serpiente come
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

