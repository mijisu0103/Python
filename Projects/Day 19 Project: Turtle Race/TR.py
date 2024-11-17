from turtle import Turtle, Screen
import random

# Initialise the value of is_race_on
is_race_on = False
# Construct a screen object
screen = Screen()
# Resize the screen
screen.setup(width=500, height=400)

# Take a user input
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ").lower()

# Turtle colour list
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
# List of turtles' y_position
y_positions = [-70, -40, -10, 20, 50, 80]
# List of all turtles
all_turtles = []


# Looping the turtle creation to create six turtles
for turtle_index in range(0, 6):
    # Construct a turtle object, shaped as a turtle
    new_turtle = Turtle(shape="turtle")
    # Change the colours of turtles
    new_turtle.color(colours[turtle_index])
    # Not drawing so no need for pen to be down
    new_turtle.penup()
    # Relocate turtle using coordinate
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    # Add each turtle to the all_turtles list
    all_turtles.append(new_turtle)

# Change the state of the race as soon as user makes their bet
if user_bet:
    is_race_on = True

# Randomise and loop the turtles' movement
while is_race_on:
    # Apply the random distance to all turtles using loop
    for turtle in all_turtles:
        # Loop end condition
        if turtle.xcor() > 230: # turtle is 40 * 40 and the end x coordinate for the screen is 250 (250 - (40 / 2))
            # Finish the race by changing the race state
            is_race_on = False
            # Create a variable to check the winning turtle's colour
            winning_colour = turtle.pencolor()
        # Check the winner and notify the user
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")

        # Randomise the turtle's movement
        rand_distance = random.randint(0, 10) # randint is the end inclusive
        turtle.forward(rand_distance)

# Change the screen to exit when the screen is clicked
screen.exitonclick()
