from turtle import Screen, Turtle
from snake import Snake
import time

# Construct a screen object
screen = Screen()

# Set up a screen
screen.setup(width=600, height=600)
# Change the background colour
screen.bgcolor("black")
# Name a programme
screen.title("My Snake Game")
#Turn off the tracer
screen.tracer(0)

# Construct a snake object from Snake class
snake = Snake()

# Set the game state to on
game_is_on = True

# Update screen every 0.1 second
while game_is_on:
    # Refresh the graphic
    screen.update()
    # Delay the animation by 0.1 second
    time.sleep(0.1)
    # Every time the screen refreshes, move snake forward by a step
    snake.move()

# Display the screen until it is clicked
screen.exitonclick()
