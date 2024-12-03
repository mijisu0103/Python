from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create a screen using Screen class
screen = Screen()
# Set the background color to black
screen.bgcolor("black")
# Set the screen size
screen.setup(width = 800, height = 600)
# Set the screen title
screen.title("Pong")
# Remove the animation
screen.tracer(0)

# Create right paddle
r_paddle = Paddle((350,0))
# Create left paddle
l_paddle = Paddle((-350,0))
# Create ball object from the ball class
ball = Ball()
# Create scoreboard object
scoreboard = Scoreboard()

# Make screen to listen for keystrokes
screen.listen()
# Make the right paddle move up when the up key is pressed
screen.onkey(r_paddle.go_up, "Up")
# Make the right paddle move down when the down key is pressed
screen.onkey(r_paddle.go_down, "Down")
# Make the left paddle move up when the "w" key is pressed
screen.onkey(l_paddle.go_up, "w")
# Make the left paddle move down when the "s" key is pressed
screen.onkey(l_paddle.go_down, "s")

# Manually update the screen and refresh it every single time
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Set the screen to disappear when it is clicked
screen.exitonclick()
