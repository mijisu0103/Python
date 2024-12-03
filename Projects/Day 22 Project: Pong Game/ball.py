from turtle import Turtle

# Create Ball class + Inherit Turtle class
class Ball(Turtle):
    # Initialise new ball object
    def __init__(self):
        super().__init__()
        # Set the ball color to white so that it is visible
        self.color("white")
        # Set the ball's shape to circle
        self.shape("circle")
        # Do not need to draw the ball moving to its start position
        self.penup()
        # Create attributes to reverse the ball's direction
        self.x_move = 10
        self.y_move = 10
        # Create attribute for a ball's speed
        self.move_speed = 0.1

    def move(self):
        # Change the x coordinate
        new_x = self.xcor() + self.x_move
        # Change the y coordinate
        new_y = self.ycor() + self.y_move
        # Move the ball's position
        self.goto(new_x, new_y)

    def bounce_y(self):
        # When the ball hits the top or the bottom wall, reverse its y direction
        self.y_move *= -1

    def bounce_x(self):
        # When the ball hits the left or the right side of the wall, reverse its x direction
        self.x_move *= -1
        # Adjust the ball speed
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        # Reset the ball speed
        self.move_speed = 0.1
