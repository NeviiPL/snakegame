from turtle import Screen
from snake import *
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake by mnichu12")
screen.tracer(0)

snakes = Snake()




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakes.move(snakes)






screen.exitonclick()