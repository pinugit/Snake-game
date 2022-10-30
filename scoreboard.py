from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto(x=-25, y=280)
        self.color("white")
        self.ht()
        self.write(f"Score : 0", font=(15))

    def write_score(self, score):
        self.clear()
        self.write(f"Score : {score}", font=(15))
