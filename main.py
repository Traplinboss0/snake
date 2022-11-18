#Importamos las librerias pertinentes para el proyecto
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#se programa la pantalla con las instrucciones
screen = Screen()
#ancho y alto de la pantalla
screen.setup(width=1200, height=600)
#color del fondo de pantalla
screen.bgcolor("green")
# Titulo que se muestra en pantalla
screen.title("My Snake Game")
#Activa y desactiva la animacion, establece un retrazo en el dibujado
screen.tracer(0.5)

#Inicializamos variables con funciones
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Con este codigo conseguimos nuestra pantalla atienda e identifique las acciones por teclado
screen.listen()
#accion de teclado mover arriba
screen.onkey(snake.up, "Up")
#accion de teclado mover abajo
screen.onkey(snake.down, "Down")
#accion de teclado mover Izquierda
screen.onkey(snake.left, "Left")
#accion de teclado mover Derecha
screen.onkey(snake.right, "Right")

#Con este codigo comenzarea el juego
game_is_on = True
#si el juego se esta ejecutando la pantalla se actualiza
while game_is_on:
    screen.update()
#tienpo de actualizacion de la panatlla
    time.sleep(0.1)
#movimiento de la serpiente
    snake.move()

    #Deteccion de la comida dela serpienta
    if snake.head.distance(food) < 15:
        #Refresca la comida para que ya no se muestre al coilisionar con la serpiente
            food.refresh()
        #funcion para que la serpiente crezca conforme come
            snake.extend()
        #incremento del puntaje
            scoreboard.increase_score()

    #Este codigo detecta la colicion con las paredes
    if snake.head.xcor() > 580 or snake.head.xcor() < -580 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
        #si la serpiente coliciona se termina el juego
        game_is_on = False
        #el final de del puntaje
        scoreboard.game_over()

    #Colision contra la cola de ls serpiente
    for segment in snake.segments:
        if segment == snake.head:
            pass
        # Detecta la distencia de la serpiente contra su cola
        elif snake.head.distance(segment) < 10:
            # si la serpiente coliciona se termina el juego
                game_is_on = False
            # el final de del puntaje
                scoreboard.game_over()
#crea la interfaz para salir de la pantalla
screen.exitonclick()













