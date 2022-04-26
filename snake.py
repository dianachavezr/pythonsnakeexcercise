from turtle import Screen, Turtle 

#Crear escenario
screen = Screen()#se instancia ó crea objeto
screen.setup(width=600, height=600)#metodo setup sale de Screen
screen.bgcolor("black")
screen.title ("Programate snake")

# creación del cuerpo de la serpiente


'''
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
positions = [(0,0),(-20,0), (-40,0)]

for position in positions:
    #goto es para mover la serpiente en las diferentes coordenadas
    snake_segment = Turtle("square")
    snake_segment.color('white')
    snake_segment.goto(position)##primer numero es X, segundo número es Y




screen.exitonclick()