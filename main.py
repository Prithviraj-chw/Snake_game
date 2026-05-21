from turtle import Turtle, Screen
import time
from snake import Snake
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0) #tracer is used to control the screen animations, 0 turns it off
#.update() is to be used when we want to update the screen when the tracer is turned off
snake = Snake()
snakes = []
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update() #without the tracer turned off, the snakes move block by block and not as one single unit
    time.sleep(0.1) #without using the timer sleep , the screen will update too fast and we cant even see the snake
    snake.move_snake()

















screen.exitonclick()