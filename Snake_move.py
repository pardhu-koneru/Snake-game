from turtle import Turtle,Screen

STARTING_POSITIONS = [(0,0),(-20,0),(-40 ,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.speed("slow")

    def create_snake(self):
        for postion in STARTING_POSITIONS:
            self.add_segment(postion)

    def add_segment(self,position):
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(20)

    def up(self):
        if(self.head.heading()!=DOWN):
            self.head.setheading(UP)
    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)
    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)
    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)