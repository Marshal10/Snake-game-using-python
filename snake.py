from turtle import Turtle

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

class Snake:
	
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
            
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
        
            
    def add_segment(self,position):
        segment=Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)
            
     
    def extend(self):
        self.add_segment(self.segments[-1].pos())
            
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)    
        
        
    def right(self):
        if self.head.heading()==180:
            return None
        self.head.setheading(0) 
    
    def up(self):
        if self.head.heading()==270:
            return None
        self.head.setheading(90)
    
    def left(self):
        if self.head.heading()==0:
            return None
        self.head.setheading(180)
    
    def down(self):
        if self.head.heading()==90:
            return None
        self.head.setheading(270)
        
    def reset(self):
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]    
        
    def hide_snake(self):
        for segment in self.segments:
            segment.hideturtle()   

    
        
       
