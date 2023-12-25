from turtle import *
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")
segments=[]
x_cor=10
for index in range(3):
    segment=Turtle(shape="square")
    
    segment.penup()
    segment.color("white")
    segment.goto(x_cor,0)
    
    x_cor-=20
    segments.append(segment)


    


while True:
    screen.update()
    time.sleep(1)    
    for seg_num in range(len(segments)-1,0,-1):
        new_x=segments[seg_num-1].xcor()
        new_y=segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)    
    segments[0].left(90) 


screen.exitonclick()