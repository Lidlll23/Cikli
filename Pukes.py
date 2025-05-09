import turtle
import random

def draw_petal(t, radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

def draw_flower(t, num_petals, radius, angle, color):
    t.color(color)
    for _ in range(num_petals):
        draw_petal(t,radius,angle)
        t.left(360 / num_petals)

screen=turtle.Screen()
screen.bgcolor("black")

flower=turtle.Turtle()
flower.speed(0)
flower.width(2)

colors=["red","orange","yellow","green","blue","purple","magenta"]

for _ in range(150):
    flower.penup()
    x=random.randint(-500,500)
    y=random.randint(-450,450)
    flower.goto(x,y)
    flower.setheading(random.randint(0,360))
    flower.pendown()
    draw_flower(
        flower,
        num_petals=random.randint(6,12),
        radius=random.randint(40,80),
        angle=random.randint(60,100),
        color=random.choice(colors)
    )
flower.hideturtle()
screen.mainloop()