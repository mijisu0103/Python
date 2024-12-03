from turtle import Turtle

# Create Paddle class + Inherit Turtle class
class Paddle(Turtle):
    # Initialise new paddle object
    def __init__(self, position):
        super().__init__()
        # Set the paddle's shape to square
        self.shape("square")
        # Set the paddle color to white so that it is visible
        self.color("white")
        # Stretch the width by 5 (to make 100 * 20 from 20 * 20)
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        # Do not need to draw the paddle moving to its start position
        self.penup()
        # Make the paddle go to the position
        self.goto(position)

    # Go up function
    def go_up(self):
        # Change the y coordinate
        new_y = self.ycor() + 20
        # Move the paddle's position
        self.goto(self.xcor(), new_y)

    # Go down function
    def go_down(self):
        # Change the y coordinate
        new_y = self.ycor() - 20
        # Move the paddle's position
        self.goto(self.xcor(), new_y)
