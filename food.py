from turtle import Turtle
from random import randint

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.penup()
        self.refresh()

    def refresh(self):
        random_x_cor=randint(-280,280)
        random_y_cor=randint(-280,280)
        self.goto(random_x_cor,random_y_cor)