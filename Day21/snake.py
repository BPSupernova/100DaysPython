from turtle import Turtle

class Snake:
    def __init__(self):
        segment1 = Turtle('square')
        segment2 = Turtle('square')
        segment3 = Turtle('square')

        segment1.setposition(20, 0)
        segment2.setposition(0, 0)
        segment3.setposition(-20, 0)

        self.segments = [segment1, segment2, segment3]
        for segment in self.segments:
            segment.color('white')
            segment.penup()

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        segment1 = Turtle('square')
        segment2 = Turtle('square')
        segment3 = Turtle('square')

        segment1.setposition(20, 0)
        segment2.setposition(0, 0)
        segment3.setposition(-20, 0)

        self.segments = [segment1, segment2, segment3]
        for segment in self.segments:
            segment.color('white')
            segment.penup()
        

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)