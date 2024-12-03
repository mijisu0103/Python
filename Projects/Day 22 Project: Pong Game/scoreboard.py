from turtle import Turtle

# Create Scoreboard class + Inherit Turtle class
class Scoreboard(Turtle):
    # Initialise new Scoreboard object
    def __init__(self):
        super().__init__()
        # Set the scoreboard color to white so that it is visible
        self.color("white")
        # Do not need to draw the scoreboard
        self.penup()
        # Do not need turtle to be able to write something
        self.hideturtle()
        # Create attributes for the scoreboard class
        self.l_score = 0
        self.r_score = 0
        # Call update_scoreboard when the scoreboard is initialised firstly and when a player score a point
        self.update_scoreboard()

    def update_scoreboard(self):
        # Erase the score for the update
        self.clear()
        # Write left-sided player's score on the screen
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        # Write right-sided player's score on the screen
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
