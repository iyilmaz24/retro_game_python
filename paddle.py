

class GamePaddle:

    MOVEMENT = 20

    def __init__(self, turt):
        self.paddle = turt
        self.paddle.pen(shown=True, pendown=False)
        self.paddle.goto(0, -225)
        self.paddle.color('white')
        self.paddle.shape(name='square')
        self.paddle.shapesize(stretch_wid=0.5, stretch_len=4)

    def move_left(self):
        self.paddle.goto(self.paddle.xcor() - GamePaddle.MOVEMENT, -225)

    def move_right(self):
        self.paddle.goto(self.paddle.xcor() + GamePaddle.MOVEMENT, -225)


