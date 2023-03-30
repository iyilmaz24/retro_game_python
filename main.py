import turtle
from game_setup import *
from paddle import *
from ball import *
from bricks import *

BRICK_COLORS = ["purple", "brown", "brown", "blue", "green"]

game_active = True

# this creates the entire screen including the background, borders, text lines,
# window size, and adds name to pop up window
turtle_arg1 = turtle.Screen()
turtle_arg2 = turtle.Turtle()
turtle_arg3 = turtle.Turtle()
creator = GameSetUp(t1=turtle_arg1, t2=turtle_arg2, t3=turtle_arg3)
creator.create_window()

# this creates the paddle and allows it to have movement from left to right
turtle_for_paddle = turtle.Turtle()
paddle = GamePaddle(turt=turtle_for_paddle)

brick_list = []

# using a for loop we can choose colors, and with the nested for loop we can create the bricks row by row
y = 215
for color in BRICK_COLORS:
    x = -217
    y -= 35
    for i in range(6):
        brick = Bricks(color=color, position=(x, y))
        x += 87
        brick_list.append(brick)

# this creates the ball for the game
turtle_ball = turtle.Turtle()
ball = GameBall(turtle_ball)

# allows player to start moving paddle
creator.window.listen()
creator.window.onkey(paddle.move_left, "Left")
creator.window.onkey(paddle.move_right, "Right")

# makes ball head random direction at game start
ball.ball_random_start()


while game_active == True:

    ball.ball_continuous_movement()

# this removes bricks after they are hit, adds points to our current score, and updates our current score on screen
    for brick in brick_list:
        if ball.ball.distance(brick) <= 40:
            ball.ball_after_hit()
            brick.hideturtle()
            brick_list.remove(brick)
            creator.update_score(5)

    if ball.ball.distance(paddle.paddle) <= 30:
        ball.ball_after_hit()


    ''' If the ball is above the hypothetical mid-line of y = 50 when it hits the wall, the ball will ricochet downwards.
    If the ball is below the line of y = 50 when it hits the wall, it will ricochet upwards.
    this helps unstick the ball and prevent situations where the ball gets stuck in a corner and keeps bouncing between
    the walls and takes a long time to come back down towards the paddle '''
    if ball.ball.xcor() < -272:
        if ball.ball.ycor() > 50:
            ball.ball_hit_wall_left_turn()
        elif ball.ball.ycor() < 50:
            ball.ball_hit_wall_right_turn()

    ''' The below if statement is the same as the above if statement on lines 68 - 72. The difference between these is
    that the above if statement is meant for the right wall while this one is for the left wall. Therefore, I had to
    reverse the logic, and write an inverse nested if + elif statement block for it to work on the left wall'''
    if ball.ball.xcor() > 273:
        if ball.ball.ycor() > 50:
            ball.ball_hit_wall_right_turn()
        elif ball.ball.ycor() < 50:
            ball.ball_hit_wall_left_turn()

# this ricochets the ball downwards if it hits the ceiling
    if ball.ball.ycor() > 273:
        ball.ball_after_hit()

# this ends the game if the ball touches the bottom border
    if ball.ball.ycor() < -271:
        game_active = False
        creator.game_over()

# this ends the game if all bricks are broken
    if len(brick_list) == 0:
        game_active = False
        creator.game_won()

creator.window.exitonclick()


# if the current score is greater than the high score stored in the highscore.txt file, it will be updated as the
# high score, and displayed next time the game is launched

file = open('highscore.txt', mode='r')
high_score = file.read()
if int(high_score) < creator.score:
    f = open('highscore.txt', mode='w')
    f.write(str(creator.score))


