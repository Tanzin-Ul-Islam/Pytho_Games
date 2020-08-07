import turtle
import time
delay=0.001
segment=[]
score=0
high_score=0

#Screen
wn=turtle.Screen()
wn.title("DX Ball by @tanzin")
wn.setup(width=800,height=600)
wn.bgcolor("green")
wn.tracer(0)
#score board
pen=turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,270)
pen.write("Score:0  High Score:0",align="center",font=("arial",18,"normal"))

#Bar
bar=turtle.Turtle()
bar.shape("square")
bar.shapesize(stretch_wid=1,stretch_len=6)
bar.color("blue")
bar.penup()
bar.goto(0,-275)

#Block
x=-380
y=250
count=0
for i in range(5):
    for j in range(14):
        block=turtle.Turtle()
        block.shape("square")
        block.shapesize(stretch_wid=1,stretch_len=2)
        if count==0:
            block.color("red")
            count=1
        elif count==1:
            block.color("blue")
            count=0
        block.penup()
        x=x+50
        block.goto(x,y)
        segment.append(block)
    x=-380
    y=y-40


#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=0.8,stretch_len=0.8)
ball.color("red")
ball.penup()
ball.goto(0,-260)
ball.dx=-2
ball.dy=2

#function
def goleft():
    x=bar.xcor()
    bar.setx(x-40)

def goright():
    x=bar.xcor()
    bar.setx(x+40)

#keyboard listner
wn.listen()
wn.onkey(goleft,"f")
wn.onkey(goright,"j")

#main loop
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor()>390:
        ball.setx(390)
        ball.dx*=-1
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx*=-1
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-260 and ball.ycor()>-280 and ball.xcor()<bar.xcor()+60 and ball.xcor()>bar.xcor()-60:
        ball.sety(-260)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.goto(bar.xcor()+20,bar.ycor()+20)

    #hide blocks
    for segments in segment:
        if ball.distance(segments) < 20:
            segments.goto(1000,1000)
            ball.dy*=-1
            score=score+5
            if score>high_score:
                high_score=score
            pen.clear()
            pen.write("Score:{}  High Score:{}".format(score,high_score), align="center", font=("arial", 18, "normal"))
            #delay = delay - 0.001



    time.sleep(delay)