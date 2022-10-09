from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",24,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,270)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"EL puntaje es: {self.score}", font=FONT, align = ALIGNMENT)

    def increase_score(self):
        self.clear()
        self.score += 1 
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Perdiste el juego :(", font=FONT, align = ALIGNMENT)
