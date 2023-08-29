from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(align=ALIGNMENT, arg=f"Score : {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(align=ALIGNMENT, arg="GAME OVER", font=FONT)
    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(align=ALIGNMENT, arg=f"Score : {self.score}", font=FONT)
