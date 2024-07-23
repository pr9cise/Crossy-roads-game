from scoreboard import Scoreboard
from turtle import Screen
from animal import Animal
from cars import Cars
import math as m
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=800, height=1000)
screen.title("highway")
screen.tracer(0)
screen.colormode(255)

animal = Animal()
scoreboard = Scoreboard()
cars = Cars()

screen.listen()
screen.onkeypress(animal.animal_up, "Up")
screen.onkeypress(animal.animal_down, "Down")

game_state = True

while game_state:
    screen.update()
    time.sleep(0.01)
    cars.pos_refresh()

    #finishing the line once
    if animal.ycor() >= 440:
        scoreboard.score_increase()
        animal.reset_pos()
        cars.speed_increase()
        animal.speed += scoreboard.score / 10

    #collisions with cars
    for i in cars.cars:
        if i.ycor() - 10 < animal.ycor() < i.ycor() + 10 and animal.distance(i) <= 30:
            game_state = False

scoreboard.game_over()
time.sleep(2)
screen.bye()
