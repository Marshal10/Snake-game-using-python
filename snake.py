from turtle import Turtle
X_COR=0
MOVE_DISTANCE=20

class Snake:
	
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
            
    def create_snake(self):
        global X_COR
        for index in range(3):
            segment=Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.goto(X_COR,0)
            
            X_COR-=20
            self.segments.append(segment)
            
            
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

    
        
       
