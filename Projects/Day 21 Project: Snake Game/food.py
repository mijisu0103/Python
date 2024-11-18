from turtle import Turtle
import random

# Create a Food class that inherits Turtle class
class Food(Turtle):
# Initialise Food class
    def __init__(self):
        # Call a superclass (Turtle class) to inherit
        super().__init__()
        # Change the Turtle shape to circle
        self.shape("circle")
        # Do not need to draw
        self.penup()
        # Resize the shape size (stretch the turtle along with the length, width)
        self.shapesize(0.5, 0.5)
        # Change the turtle color
        self.color("blue")
        # Change the turtle speed
        self.speed("fastest")
        # Relocate the food
        self.refresh()

# Relocate the food after collision
    def refresh(self):
        # Create a randomised coordinate x and y
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        # Move food to randomised coordinate
        self.goto(random_x, random_y)

