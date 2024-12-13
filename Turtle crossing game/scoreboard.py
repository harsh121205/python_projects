FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,270)
        self.score = 0
    def game_over(self):
        self.teleport(-50, 0)
        self.write(arg='GAME OVER',font=FONT)
    def level(self):
        self.write(arg=f'Level: {self.score}',font=FONT)
