from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.total_segments = 3
        self.segments_list = []

    def make_snake(self):
        x_cord = 0
        for i in range(self.total_segments):
            a_segment = Turtle(shape="square")
            a_segment.color("white")
            a_segment.penup()
            a_segment.goto(x=x_cord, y=0)
            self.segments_list.append(a_segment)
            x_cord -= 20

    def move(self):
        segment_list = self.segments_list
        for i in range(len(segment_list) - 1, 0, -1):
            # getting the x coordinate value of it's front segment from the segment list
            new_x = segment_list[i - 1].xcor()
            # getting the y coordinate value of it's front segment from the segment list
            new_y = segment_list[i - 1].ycor()
            # assigning tht x and y coordinate value to the current segment
            segment_list[i].goto(new_x, new_y)
        segment_list[0].forward(MOVE_DISTANCE)
