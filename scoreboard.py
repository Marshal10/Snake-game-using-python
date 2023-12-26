from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",14,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0 
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle() 
        
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)