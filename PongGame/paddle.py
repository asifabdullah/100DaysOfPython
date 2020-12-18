from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=1)
        self.penup()
        self.goto(position[0], position[1])

    def up(self):
        position = self.pos()
        if position[1] < 280:
            self.goto(position[0], position[1] + 20)

    def down(self):
        position = self.pos()
        if position[1] > -280:
            self.goto(position[0], position[1] - 20)
