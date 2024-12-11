from turtle import Turtle

class Score(Turtle) :
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score_1 = 0
        self.score_2 = 0
        self.goto(-100, 200)
        self.write(arg=f'{self.score_1}', font=('Arial', 70, 'normal'))
        self.goto(70, 200)
        self.write(arg=f'{self.score_2}', font=('Arial', 70, 'normal'))

    def scoreone(self,x):
        if x > 0 :
            self.score_1  += 1
        self.goto(-100,200)
        self.write(arg=f'{self.score_1}',font=('Arial',70,'normal'))
    def scoretwo(self,x):
        if x < 0 :
            self.score_2 += 1
        self.goto(70, 200)
        self.write(arg=f'{self.score_2}', font=('Arial', 70, 'normal'))







