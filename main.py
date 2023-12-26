from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

        

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")



snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on=True
boundary=300
upper_boundary=320
left_boundary=320
while game_on:
    screen.update()
    time.sleep(0.1)    
    snake.move()
    if snake.head.distance(food)<15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()
        
        
    if len(snake.segments)==3:
        boundary=280
        upper_boundary=300
        left_boundary=300
        
    if snake.head.xcor()>boundary or snake.head.xcor()<-left_boundary or snake.head.ycor()>upper_boundary or snake.head.ycor()<-boundary:
        game_on=False
        scoreboard.game_over()
        
        
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_on=False
            scoreboard.game_over()
            break
            
    
screen.exitonclick()