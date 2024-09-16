import time
from Snake_move import Snake
from turtle import Turtle,Screen
from ScoreBoard import ScoreBoard
from Food import Food

screen = Screen()
screen.tracer(0) # to trace the segments without caterpillar movement
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My snake game")


snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
game_is_on = True

while game_is_on:
    screen.update()  # linked with the tracer study about this
    time.sleep(0.1)
    snake.move()

    #DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15: # DISTANCE IS USED TO FIND THE DISTANCE B/W TO TURTLES
        food.refresh()
        snake.extend()
        score.score_update()

    # DETECT COLLISION WITH WALL
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor()>290 or snake.head.ycor() < -290:
        score.game_over()
        game_is_on = False

    # DETECT COLLISION WITH Tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()ch