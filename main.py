from turtle import Screen
from snake import Snake
from scoreboard import ScoreBoard
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My turtle game")
screen.tracer(0)

tom = Snake()
tom.make_snake()
tom_food = Food()

screen.listen()
screen.onkey(fun=tom.turn_up, key="Up")
screen.onkey(fun=tom.turn_down, key="Down")
screen.onkey(fun=tom.turn_right, key="Right")
screen.onkey(fun=tom.turn_left, key="Left")

is_game_running = True
score = 0
scoreboard = ScoreBoard()
while is_game_running:
    tom.move()
    # screen.wri

    # checking the distance between the food and the snake head
    if tom.segments_list[0].distance(tom_food) < 14:
        tom_food.refresh()
        tom.grow()
        score += 1
        scoreboard.write_score(score)
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
