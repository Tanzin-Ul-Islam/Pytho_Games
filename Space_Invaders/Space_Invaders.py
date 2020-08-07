import turtle
import winsound
import time
import math
#import random

bulletstate="ready"
delay=0.00001
segment=[]
segment2=[]
dx = 2
dy = -20
score=0
highscore=0


wn=turtle.Screen()
wn.setup(width=600,height=600)
wn.bgcolor("black")
wn.tracer(0)
#wn.bgpic("IrF.gif")

#register gif
wn.register_shape("invader.gif")
wn.register_shape("player.gif")

#score board
sc=turtle.Turtle()
sc.shape("square")
sc.color("green")
sc.hideturtle()
sc.penup()
sc.setposition(-250,250)
sc.write("Score:0  High Score:0",align="left",font=("arial",10,"normal"))


#set boarder
bd=turtle.Turtle()
bd.speed(0)
bd.color("white")
bd.penup()
bd.goto(-270,-270)
bd.pendown()
bd.pensize(3)
for i in range(4):
    bd.forward(540)
    bd.left(90)
bd.hideturtle()


#Player
pl=turtle.Turtle()
pl.shape("player.gif")
pl.left(90)
pl.penup()
pl.goto(0,-255)
pl.speed=0

#player bullet
bullet=turtle.Turtle()
bullet.shape("triangle")
bullet.color("red")
bullet.shapesize(stretch_wid=0.5,stretch_len=0.5)
bullet.penup()
bullet.left(90)
bullet.hideturtle()


#enemy
r=-240
s=240
for i in range(4):
    for j in range(8):
        eni=turtle.Turtle()
        eni.shape("invader.gif")
        eni.speed(0)
        eni.penup()
        r=r+50
        eni.goto(r,s)
        segment.append(eni)
    r=-240
    s=s-50

#function
def goright():
    pl.speed=7

def goleft():
    pl.speed=-7

def move_player():
    x=pl.xcor()
    x+=pl.speed
    if x>250:
        x=250
    if x<-250:
        x=-250
    pl.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        winsound.PlaySound("shoot.wav",winsound.SND_ASYNC)
        x=pl.xcor()
        y=pl.ycor()+20
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<20:
        return True
    else:
        return False





#keyboard binding
wn.listen()
wn.onkey(goright,"Right")
wn.onkey(goleft,"Left")
wn.onkey(fire_bullet,"space")



#main loop
while True:
    wn.update()
    move_player()
    for en in segment:
        en.setx(en.xcor()+dx)
        if en.xcor()>250:
            for e in segment:
                e.sety(e.ycor()+dy)
            dx *= -1
        if en.xcor()<-250:
            for e in segment:
                e.sety(e.ycor()+dy)
            dx *= -1

        #collision with enemy and bullet
        if isCollision(bullet,en):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
            en.setposition(0,1000)
            score=score+5
            if score>highscore:
                highscore=score
        sc.clear()
        sc.write("Score:{}  High Score:{}".format(score,highscore), align="left", font=("arial", 10, "normal"))

        #collision with player and enemy
        if isCollision(pl, en):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            pl.hideturtle()
            pl.goto(0,1000)
            en.hideturtle()

    if bulletstate == "fire":
        y = bullet.ycor() + 15
        bullet.sety(y)
        if bullet.ycor() > 270:
            bullet.hideturtle()
            bulletstate = "ready"





    time.sleep(delay)