from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
game_score = 0
screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0) #tracer is used to control the screen animations, 0 turns it off
#.update() is to be used when we want to update the screen when the tracer is turned off
snake = Snake()
food = Food()
score = Scoreboard()
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

    #detect collision with food & wall
    if snake.head.distance(food) < 15: # .distance calculates the dist between our object and the one inside the ()
        food.refresh()
        snake.extend_snake()
        score.clear()
        score.update_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    #detect collision with tail (list slicing)
    for segment in snake.snake_segments[1:]: #get hold of everything except the snake's head
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()




















screen.exitonclick()