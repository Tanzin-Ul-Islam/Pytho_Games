import turtle
import time
delay=0.005
#score
Player1=00
Player2=00

#screen
wn=turtle.Screen()
wn.title("Pong Game by @tanzin")
wn.bgcolor("blue")
wn.setup(width=800,height=600)
wn.tracer(0)

#scoreboard
pen=turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,250)
pen.write("Player1:0  Player2:0",align="center",font=("Arial",25,"normal"))


#Bar a
Bar_a=turtle.Turtle()
Bar_a.speed(0)
Bar_a.shape("square")
Bar_a.shapesize(stretch_wid=5,stretch_len=1)
Bar_a.color("white")
Bar_a.penup()
Bar_a.goto(-350,0)

#Bar b
Bar_b=turtle.Turtle()
Bar_b.speed(0)
Bar_b.shape("square")
Bar_b.shapesize(stretch_wid=5,stretch_len=1)
Bar_b.color("white")
Bar_b.penup()
Bar_b.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.goto(0,0)
ball.penup()
ball.dx=2
ball.dy=2

#function
def Bar_a_goup():
    y=Bar_a.ycor()
    Bar_a.sety(y+30)
def Bar_a_godown():
    y=Bar_a.ycor()
    Bar_a.sety(y-30)
def Bar_b_goup():
    y=Bar_b.ycor()
    Bar_b.sety(y+30)
def Bar_b_godown():
    y=Bar_b.ycor()
    Bar_b.sety(y-30)

#if Bar_a.ycor()>300 or Bar_a.ycor()<-300:
    #Bar_a.d

#Keyboard listen
wn.listen()
wn.onkey(Bar_a_goup,"e")
wn.onkey(Bar_a_godown,"d")
wn.onkey(Bar_b_goup,"i")
wn.onkey(Bar_b_godown,"k")

#main loop
while True:
    wn.update()

#move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#Bars Limit
    if Bar_a.ycor()>290:
        Bar_a.sety(290)
    if Bar_a.ycor() <-290:
        Bar_a.sety(-290)
    if Bar_b.ycor() > 290:
        Bar_b.sety(290)
    if Bar_b.ycor()<-290:
        Bar_b.sety(-290)

#Bouncing ping
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        Player1 += 5
    pen.clear()
    pen.write("Player1:{}  Player2:{}".format(Player1, Player2), align="center", font=("Arial", 25, "normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        Player2 += 5
    pen.clear()
    pen.write("Player1:{}  Player2:{}".format(Player1, Player2), align="center", font=("Arial", 25, "normal"))


    if(ball.xcor()>340 and ball.xcor()<360 and ball.ycor()<Bar_b.ycor()+50 and ball.ycor()>Bar_b.ycor()-50):
        ball.setx(340)
        ball.dx *=-1
    if(ball.xcor()<-340 and ball.xcor()>-360 and ball.ycor()<Bar_a.ycor()+50 and ball.ycor()>Bar_a.ycor()-50):
        ball.setx(-340)
        ball.dx *=-1
    time.sleep(delay)





