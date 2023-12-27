from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",14,"normal")

    
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0 
        with open("data.txt") as data:
            self.high_score=int(data.read())
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
            with open("data.txt","w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.clear()    
        self.update_score()
        
        return True
           
