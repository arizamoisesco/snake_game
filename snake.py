from turtle import  Turtle

START_POSITION = [(0,0),(-20,0),(-40,0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    #Metodo similar funcion
    def __init__(self):
        self.segments = [] #Atributo
        self.create_snake()
        self.head = self.segments[0]
        
    #Creación del cuerpo de la serpiente    
    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)
            
    
    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    #movimiento de la serpiente
    def move(self):
        for segment_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment_num -1].xcor()
            new_y = self.segments[segment_num -1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
    
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)






    
        


