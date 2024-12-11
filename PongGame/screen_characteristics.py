from turtle import Turtle

class Features(Turtle) :
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(1.5,0.25)
        self.goto(0,-290)
        while self.ycor() < 290 :
            self.stamp()
            self.teleport(0,self.ycor()+50)


