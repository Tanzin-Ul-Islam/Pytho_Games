import turtle
import time
import random

delay=0.18
score=0
high_score=0
count=0

#setup the screen
wn=turtle.Screen()
wn.title("Snake Game by Tanzin")
wn.bgcolor("Green")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Blue")
food.penup()
food.goto(0, 100)
segments = []

#ScoreBoard
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0  High Score:0",align="center",font=("Arial",25,"normal"))

#obstacl



#function
def go_up():
    if head.direction!="down":
        head.direction="up"

def go_down():
    if head.direction!="up":
        head.direction="down"

def go_left():
    if head.direction!="right":
        head.direction="left"

def go_right():
    if head.direction!="left":
        head.direction="right"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y + 20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y - 20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x - 20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x + 20)

#keyboard binding
wn.listen()
wn.onkey(go_up,"e")
wn.onkey(go_down,"c")
wn.onkey(go_left,"s")
wn.onkey(go_right,"f")

#main game loop
while True:
    wn.update()
    #check for collision
    if head.xcor() > 290:
        x = head.xcor()
        head.setx(x - 590)
    if head.xcor()<-290:
        x = head.xcor()
        head.setx(x + 590)
    if head.ycor()>290:
        y = head.ycor()
        head.sety(y - 590)
    if head.ycor()<-290:
        y = head.ycor()
        head.sety(y + 590)


    if head.distance(food)<20:
    #move food
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
    #add segments
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)
        delay-=0.001
    #setting score and high score
        score=score+5

        if high_score<score:
            high_score=score
        pen.clear()
        pen.write("Score:{}  High Score:{}".format(score,high_score),align="center",font=("Arial",25,"normal"))


    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()
    #collision of head with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            score = 0
            pen.clear()
            pen.write("Score:{}  High Score:{}".format(score, high_score), align="center", font=("Arial", 25, "normal"))
            for segment in segments:
                segment.goto(1000,1000)
            segments=[]
    time.sleep(delay)

#wn.mainloop()