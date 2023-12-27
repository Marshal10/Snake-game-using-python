from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",14,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0 
        self.high_score=0
        self.penup()
        self.color("white")
        self.update_score()
        self.hideturtle()
        
    def update_score(self):
        self.clear()
        self.goto(-80,280)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)     
        self.goto(80,280)
        self.write(f"High Score: {self.high_score}",align=ALIGNMENT,font=FONT)
        
    def increase_score(self):
        self.score+=1
        self.update_score()
        
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        self.clear()    
        self.update_score()
        
        return True
           
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over.",align=ALIGNMENT,font=FONT)