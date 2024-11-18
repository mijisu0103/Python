from turtle import Turtle

# Position list for segments in list
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Set a distance that a snake moves in constant
MOVE_DISTANCE = 20
# Constants for directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

# Define what happens when the class gets initialised
    def __init__(self):
        # Create a list for segments
        self.segments = [] # Need to use self. when working with a class
        # Call a create_snake() method here to create a snake
        self.create_snake()
        # Set the first segment equal to the head attribute (= Set the first segment as the snake's head)
        self.head = self.segments[0]

# Create a snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Initialise segment object and set its shape to square
        new_segment = Turtle(shape="square")
        # Set its colour as white
        new_segment.color("white")
        # Do not need to draw
        new_segment.penup()
        # Position segment to the coordinate that is currently on loop
        new_segment.goto(position)
        # Add created segments to the segments list
        self.segments.append(new_segment)

# Extend the length of the snake
    def extend(self):
        # Add a new segment to the snake
        self.add_segment(self.segments[-1].position()) # position method comes from Turtle class

# Move a snake
    def move(self):
        # Loop in a reverse order to link segments' movements and form a snake
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Move linked segments (snake)
        self.head.forward(MOVE_DISTANCE)

# Turn snake upwards
    def up(self):
        if self.head.heading() != DOWN: # heading() is a turtle's method to check its direction (in number e.g. 90 - N)
            self.head.setheading(UP)

# Turn snake downwards
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

# Turn snake leftwards
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

# Turn snake rightwards
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

