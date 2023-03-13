import turtle;
from juggling_ball import Ball

WIDTH = 600
HEIGHT = 600

window = turtle.Screen()
window.setup(WIDTH, HEIGHT)
window.tracer(0)

ball = Ball(WIDTH, HEIGHT)
while True:
    ball.move()
    window.update()

turtle.done