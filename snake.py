SNAKE_POSITIONS = [(0,0) , (20,0) , (40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from turtle import Turtle
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for position in SNAKE_POSITIONS:
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(position)
            self.snake_segments.append(snake)

    def move_snake(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_xcoor = self.snake_segments[seg_num - 1].xcor()
            new_ycoor = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_xcoor, new_ycoor)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_segments[0].heading() != DOWN:
            self.snake_segments[0].setheading(UP)

    def down(self):
        if self.snake_segments[0].heading() != UP:
            self.snake_segments[0].setheading(DOWN)

    def left(self):
        if self.snake_segments[0].heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)

    def right(self):
        if self.snake_segments[0].heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)