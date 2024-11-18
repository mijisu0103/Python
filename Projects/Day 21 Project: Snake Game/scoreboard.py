# scoreboard.py
from turtle import Turtle

# Constants for scoreboard alignment and font
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Create a Scoreboard class that inherits Turtle class
class Scoreboard(Turtle):
# Initialise Scoreboard class
    def __init__(self):
        # Call a superclass (Turtle class) to inherit
        super().__init__()
        # Initialise score
        self.score = 0
        # Change the font color
        self.color("white")
        # No need for drawing
        self.penup()
        # Move the scoreboard to the top of the screen
        self.goto(0, 270)
        # Write a score on the screen
        self.update_scoreboard()
        # Don't need to see the arrow as just need a score written on the screen
        self.hideturtle()

    def update_scoreboard(self):
        # Write a score on the screen
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

		def increase_score(self):
        # Increase a score by 1 point
        self.score += 1
        # Clear the previous text that was written
        self.clear()
        # Write a score on the screen
        self.update_scoreboard()

