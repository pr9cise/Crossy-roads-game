from turtle import Turtle


class Animal(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.speed = 5
        self.setheading(90)
        self.up()
        self.sety(-450)
        self.shapesize(stretch_len=1, stretch_wid=1)

    def reset_pos(self):
        self.sety(-450)

    def animal_up(self):
        if self.ycor() < 450:
            self.forward(self.speed)

    def animal_down(self):
        if self.ycor() > -450:
            self.forward(-self.speed)
