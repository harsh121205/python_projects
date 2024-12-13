import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(key="Up",fun=player.movement)
cars = []
scoreboard = Scoreboard()
scoreboard.level()

for i in range(7) :
    car = CarManager()
    cars.append(car)
j = 0
modulo = 15
increment = 0
sleeptime = 0.15
game_is_on = True
while game_is_on:
    time.sleep(sleeptime)
    screen.update()
    for car in cars :
        car.move()
        car.increment = increment
        if player.distance(car) < 20 :
            screen.clear()
            scoreboard.level()
            scoreboard.game_over()
            game_is_on = False
            break
    if player.ycor() > 280 :
        scoreboard.score += 1
        scoreboard.clear()
        scoreboard.level()
        player.teleport(0,-280)
        increment += 1

        sleeptime *= 0.9
    j+=1
    if j % modulo == 0:
        for i in range(3):
            car = CarManager()
            cars.append(car)
screen.exitonclick()







