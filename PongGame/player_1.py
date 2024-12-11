from player_characteristics import Player
class PlayerOne(Player) :
    def __init__(self):
        super().__init__()
        self.goto(-390,0)
        self.left(90)
        self.speed(0)
    def up(self):
        self.goto(self.xcor(),self.ycor() + 20)
    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)


