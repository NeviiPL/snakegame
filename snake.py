from turtle import Turtle


class Snake:

    def __init__(self):
        return


    def new_snake(self):
        snake_square_pos_x = 0
        snake_body = []
        for new_snake in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.speed("slow")
            new_segment.goto(x=snake_square_pos_x, y=0)
            snake_body.append(new_segment)
            snake_square_pos_x -= 20

    def move(self, snake_body):
        for seg_num in range(len(snake_body) - 1, 0, -1):
            new_x = snake_body[seg_num - 1].xcor()
            new_y = snake_body[seg_num - 1].ycor()
            snake_body[seg_num].goto(new_x, new_y)
        snake_body[0].forward(20)
