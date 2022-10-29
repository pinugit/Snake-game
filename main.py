from turtle import Turtle, Screen
import time

from snake import Snake

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My turtle game")
screen.tracer(0)
tom = Snake()
tom.total_segments = 3
tom.make_snake()
is_game_running = True
while is_game_running:
    screen.update()
    time.sleep(0.5)
    print("in while loop")
    tom.move()

screen.exitonclick()
