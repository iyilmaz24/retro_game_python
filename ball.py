import random


# this class creates the ball and gives it behavior

class GameBall:

    def __init__(self, turtl):
        self.ball = turtl
        self.ball.pen(shown=True, pendown=False)
        self.ball.goto(0, 0)
        self.ball.color('white')
        self.ball.shape(name='circle')
        self.ball.shapesize(stretch_wid=0.85, stretch_len=0.85)

        # we use later in our methods to randomly determine where the ball heads when game starts and after contact
        self.random = 0
        self.random_dir = 0

    def ball_random_start(self):
        self.ball.right(90)
        self.random = random.randint(15, 25)
        self.random_dir = random.randint(1, 3)

        if self.random_dir == 1:
            self.ball.left(self.random)
        elif self.random_dir == 2:
            self.ball.right(self.random)

    def ball_after_hit(self):
        self.ball.right(180)
        self.random = random.randint(10, 25)
        self.random_dir = random.randint(1, 3)

        if self.random_dir == 1:
            self.ball.left(self.random)
        elif self.random_dir == 2:
            self.ball.right(self.random)

    def ball_hit_wall_right_turn(self):
        self.ball.right(90)
        self.random = random.randint(10, 25)
        self.random_dir = random.randint(1, 3)

        if self.random_dir == 1:
            self.ball.left(self.random)
        elif self.random_dir == 2:
            self.ball.right(self.random)

    def ball_hit_wall_left_turn(self):
        self.ball.left(90)
        self.random = random.randint(10, 25)
        self.random_dir = random.randint(1, 3)

        if self.random_dir == 1:
            self.ball.left(self.random)
        elif self.random_dir == 2:
            self.ball.right(self.random)

    def ball_continuous_movement(self):
        self.ball.forward(3)
