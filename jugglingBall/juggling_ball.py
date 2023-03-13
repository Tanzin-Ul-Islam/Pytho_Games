import random;
import turtle;

class Ball(turtle.Turtle):
    max_velocity = 5
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.shape("circle")
        self.color(
            random.random(),
            random.random(),
            random.random(),
        )
        self.penup()
        self.setposition(
            random.randint(-self.width // 2, self.width // 2),
            random.randint(-self.height // 2, self.height // 2),
        )
        self.setheading(90)
        self.velocity = random.randint(1, self.max_velocity)
    def move(self):
        self.forward(self.velocity)
