#importamos librerias
from turtle import Turtle
#posicion inicial de la serpiente
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,
0)]
#grado de movimiento de los botones
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#se crea clase snake
class Snake:

#iniciamos funcion
    def __init__(self):
        #asignamos parametros que se utilizaran mas tarde
        self.segments = []
        #crea a la serpiente
        self.create_snake()
        #posicion de la cabeza de la serpiente
        self.head = self.segments[0]

#utilizamos funcion crear serpiente
    def create_snake(self):
        #posicion inicial
        for position in STARTING_POSITIONS:
            #se agrega un segmento de posicion
            self.add_segment(position)

#asignamos funcion para añadir un segmento
    def add_segment(self, position):
        #forma de la serpiente
        new_segment = Turtle("circle")
        #el tamaño de lso segmentos de la serpiente
        new_segment.shapesize(stretch_len=2, stretch_wid=1)
        #color de la serpiente
        new_segment.color("blue")
        #para que no muestre el trazo
        new_segment.penup()
        #para la posicion de la serpiente
        new_segment.goto(position)
        #para que se cree mas serpiente
        self.segments.append(new_segment)

    #funcion para la extencion de la serpiente
    def extend(self):
        #añade un nuevo segmento en la cola de la serpiente
        self.add_segment(self.segments[-1].position())
    #la de movimiento al segmento
    def move(self):
        #el nunmero de segmentos que hay
        for seg_num in range(len(self.segments)- 1, 0, -1):

            #agregar nuevo segmento en los ejes x,y
            new_x = self.segments[seg_num -1].xcor()
            #agregar nuevo segmento en los ejes x,y
            new_y = self.segments[seg_num -1].ycor()
            #realiza la funcion de mover los segmentos x,y
            self.segments[seg_num].goto(new_x,new_y)
        #mueve la cabeza juntos los segmentos
        self.head.forward(MOVE_DISTANCE)

    #funcion para mover arriba
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    #funcion para mover abajo
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    #funcion para mover izquierda
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    #funcion para mover derecha
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)