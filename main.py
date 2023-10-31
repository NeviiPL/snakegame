from turtle import Screen
import snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake by mnichu12")
screen.tracer(0)

snejk = snake.Snake()

snaczek = snejk.new_snake()

print(snaczek)


# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)






screen.exitonclick()