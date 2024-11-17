# # To extract colours
# import colorgram
#
# rgb_colours = []
# # Extract RGB colours in tuples from the image
# colours = colorgram.extract('../image.jpg', 30)
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)
#
# print(rgb_colours)

import turtle as turtle_module
import random

# Change turtle's color mode to 255
turtle_module.colormode(255)

# Construct turtle object
tim = turtle_module.Turtle()
# Change turtle's speed
tim.speed("fastest")
# No need for drawing as dots are being painted
tim.penup ()
# Hide turtle to not see the arrow
tim.hideturtle()
colour_list = [(142, 152, 198), (231, 194, 217), (57, 115, 134), (185, 174, 219), (0, 59, 54), (188, 155, 171), (224, 173, 193), (1, 94, 109), (0, 69, 77), (252, 203, 184), (107, 129, 153), (24, 83, 80), (252, 170, 166), (203, 186, 223), (53, 93, 90), (117, 95, 107), (100, 134, 152), (150, 113, 132), (203, 151, 148), (52, 64, 79), (111, 85, 85), (189, 105, 99), (63, 50, 58), (80, 54, 61)]

# Change the turtle's heading for the starting point
tim.setheading(225) # midpoint of 180 and 270
tim.forward(300) # 50 paces times 5 + 50 to have enough space for dots
tim.setheading(0) # Change heading to make turtle move to the right direction
number_of_dots = 100 # 10 * 10

# Loop turtle's movement & colour randomisation
for dot_count in range (1, number_of_dots + 1):
    tim.dot(20, random.choice(colour_list)) # Randomise colour choices
    tim.forward(50) # Move turtle

    if dot_count % 10 == 0:
        # Create a new line
        tim.setheading(90) # Rotate turtle to face up
        tim.forward(50) # Move turtle by 50 paces
        tim.setheading(180) # Rotate turtle to face left
        tim.forward(500) # 5 * 100
        tim.setheading(0) # Rotate turtle to face right


# Create screen object
screen = turtle_module.Screen()
# Change the screen's behaviour
screen.exitonclick()
