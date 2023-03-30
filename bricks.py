from turtle import Turtle


# this class creates each brick as .Turtle() and gives them their appearance

class Bricks(Turtle):

    def __init__(self, color, position):
        super().__init__()
        self.shape("square")
        self.speed(10)
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=1.2, stretch_len=4)
        self.goto(position)
