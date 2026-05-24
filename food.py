from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5) #makes the food size 10x10 pixels
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # our screen stretches from +300 to -300 both in x and y direction
        random_x = random.randint(-240, 240)  # we don't want our food to spawn right at the edge of screen
        random_y = random.randint(-240, 240)
        self.goto(random_x, random_y)
