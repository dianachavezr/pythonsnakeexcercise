from turtle import Screen, Turtle, xcor
import time

from sqlalchemy import true 

#Crear escenario
screen = Screen()#se instancia ó crea objeto
screen.setup(width=600, height=600)#metodo setup sale de Screen
screen.bgcolor("black")
screen.title ("Programate snake")

screen.tracer(0)#DESACTIVAR EL EFECTO Animación por defecto


# creación del cuerpo de la serpiente


'''
Codigo por segmentos:
snake_segment = Turtle("square")
snake_segment.color('white')

#goto es para mover la serpiente en las diferentes coordenadas
snake_segment2 = Turtle("square")
snake_segment2.color('white')
snake_segment.goto(-20,0)##primer numero es X, segundo número es Y

snake_segment3 = Turtle("square")
snake_segment3.color('white')
snake_segment3.goto(-40,0)

'''

#tuplas = COORDENADAS
starting_positions = [(0,0),(-20,0), (-40,0)]
segments = []#para guardar los segmentos

#Codigo con ciclo FOR
for position in starting_positions:
    #goto es para mover la serpiente en las diferentes coordenadas
    snake_segment = Turtle("square")
    snake_segment.color('white')
    snake_segment.penup()
    snake_segment.goto(position)##primer numero es X, segundo número es Y
    segments.append(snake_segment) #agregar elementos a la lista segments

game_is_on = True ## True y False siempre con mayusculas


#movimiento de la serptiente
while game_is_on:
    screen.update()#refresca la pantalla
    time.sleep(0.2)#para jugar con el tiempo del movimiento de la serpiente
    
    '''
    for segment in segments:
        segment.forward(20)
        segments[0].left(90)
    '''    
    for seg_num in range(len(segments) -1, 0,-1):
        new_x=segments[seg_num - 1].xcor()
        new_y=segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()