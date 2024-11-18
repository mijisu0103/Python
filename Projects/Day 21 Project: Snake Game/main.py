from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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

# Construct a food object from Food class (Initialise food)
food = Food()

# Construct a scoreboard object from Scoreboard class
scoreboard = Scoreboard()

# Start listening for keystrokes
screen.listen()

# Listen for arrow keys
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        # Relocate the food
        food.refresh()
        # Extend the snake
        snake.extend()
        # Increase the score on the score board
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # Change the game state to end the snake movement and the game
        game_is_on = False
        # Display the GAME OVER text at the center of the screen
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Display the screen until it is clicked
screen.exitonclick()
