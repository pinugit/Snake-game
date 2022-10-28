from turtle import Turtle, Screen, screensize

screen = Screen()


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My turtle game")

# starting_position = [(0, 0), (-20, 0), (-40, 0)]

# for positon in starting_position:
#     segement = Turtle(shape="square")
#     segement.color("white")
#     segement.penup()
#     segement.goto(positon)


screen.exitonclick()
