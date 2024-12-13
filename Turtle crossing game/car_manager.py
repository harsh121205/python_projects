COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
from turtle import Turtle
import random
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1,2)
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.teleport(random.randint(290, 360), random.randint(-265, 265))
        self.increment = 0
    def move(self):
        self.forward(STARTING_MOVE_DISTANCE + self.increment*MOVE_INCREMENT)






