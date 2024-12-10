from idlelib.configdialog import font_sample_text
from turtle import Turtle

class Score(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,278)
        self.color('white')
        self.write(arg=f'Score:{self.score}',align='center',font=('arial',20,'normal'))
    def score_update(self):
        self.score +=1
        self.clear()
        self.write(arg=f'Score:{self.score}', align='center', font=('arial', 20, 'normal'))
    def game_over(self):
        self.home()
        self.write(arg='Game Over', align='center', font=('arial', 20, 'normal'))


