from random import randint
from turtle import Turtle

NUMBER_OF_CARS = 60

class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.moving_speed = 2
        for i in range(NUMBER_OF_CARS):
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2.2)
            new_car.up()
            new_car.color((randint(0, 255), randint(0, 255), randint(0, 255)))
            new_car.setheading(180)
            new_car.setpos(randint(400, 1580), randint(-420, 420))
            self.cars.append(new_car)

    def pos_refresh(self):
        for i in self.cars:
            if i.xcor() > -450:
                i.forward(self.moving_speed)
            elif i.xcor() <= -450:
                i.color((randint(0, 255), randint(0, 255), randint(0, 255)))
                i.setpos(randint(400, 780), randint(-420, 420))

    def speed_increase(self):
        self.moving_speed += 1