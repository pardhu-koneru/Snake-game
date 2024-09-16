from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")# COLOR SHOULD BE CHANGED FIRST
        self.penup()
        self.goto(0, 265)
        self.text_update()
        self.hideturtle()#TO HIDE THE ARROW TURTLE
    def text_update(self):
        self.write(f"Score : {self.score}", False, align="center", font=("Arial", 22, "normal"))
    def score_update(self):
        self.score += 1
        self.clear()
        self.text_update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=("Arial", 22, "normal"))