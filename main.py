from turtle import *
from snake import Snake
import time

        

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")



snake=Snake()
    


while True:
    screen.update()
    time.sleep(1)    
    snake.move()


screen.exitonclick()