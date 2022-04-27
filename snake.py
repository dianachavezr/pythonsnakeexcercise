from turtle import  Turtle

    #tuplas = COORDENADAS
STARTING_POSITION = [(0,0),(-20,0), (-40,0)]#constante se crea siempre con mayusculas

# creación del cuerpo de la serpiente
class Snake:

    def __init__(self):  #crear el constructor
        self.segments = []#atributo para guardar los segmentos
        self.create_snake()#metodo encargado de crear la serpiente:
  
  
    def create_snake(self): #creación de método
        #Codigo con ciclo FOR
        for position in STARTING_POSITION:
            #goto es para mover la serpiente en las diferentes coordenadas
            snake_segment = Turtle("square")
            snake_segment.color('white')
            snake_segment.penup()
            snake_segment.goto(position)##primer numero es X, segundo número es Y
            self.segments.append(snake_segment) #agregar elementos a la lista self.segments    


    #metodo movimiento de la 
    def move(self):
        for seg_num in range(len(self.segments) -1, 0,-1):
            new_x=self.segments[seg_num - 1].xcor()
            new_y=self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)
        #segments[0].left(90)
