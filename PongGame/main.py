from turtle import Screen
from time import sleep
from player_1 import PlayerOne
from player_2 import PlayerTwo
from screen_characteristics import Features
from python_projects.PongGame.ball import Ball
from score import Score
sleep(1)
screen = Screen()
screen.title('PONG')
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.tracer(0)
p1 = PlayerOne()
p2 = PlayerTwo()
screen_features = Features()
ball = Ball()
score = Score()
screen.listen()
screen.onkey(key="Up",fun=p2.up)
screen.onkey(key="Down",fun=p2.down)
screen.onkey(key="w",fun=p1.up)
screen.onkey(key="s",fun=p1.down)
game_is_on = True
while game_is_on :
    sleep(ball.move_ball)
    screen.update()

    print(ball.xcor())
    ball.move()

    if ball.ycor() > 290 or ball.ycor() <-290 :
        ball.bounce_y()
    if ball.distance(p1) < 30 and ball.xcor() < -370 :
        ball.bounce_x()
        ball.move_ball *= 0.95
    if ball.distance(p2) < 30 and ball.xcor() > 370:
        ball.bounce_x()
    if ball.xcor() > 400 or ball.xcor() < -400 :
        ball.move_ball = 0.1
        x= ball.xcor()
        score.clear()
        score.scoreone(x)
        score.scoretwo(x)
        ball.home()
        ball.bounce_x()














screen.exitonclick()
