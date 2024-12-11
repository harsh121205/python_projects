from turtle import Turtle

class Ball(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.60,0.60)
        self.color('white')
        self.xmove = 10
        self.ymove = 10
        self.move_ball = 0.1

    def move(self):
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x,y)
    def bounce_y(self):
        self.ymove *= -1
    def bounce_x(self):
        self.xmove *= -1



