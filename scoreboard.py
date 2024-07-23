from turtle import Turtle

FONT_NAME = "Courier"
FONT_SIZE = 24
FONT_MODE = "bold"
ALIGNMENT = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.score = 0
        self.color("black")
        self.font = (FONT_NAME, FONT_SIZE, FONT_MODE)
        self.refresh()

    def score_increase(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.setpos(-350, 450)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=self.font)

    def game_over(self):
        self.setpos(0, 450)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=self.font)
