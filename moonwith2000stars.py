import turtle
import random

t = turtle.Turtle()

t.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")
t.pencolor("white")
t.penup()
t.goto(-300,180)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(70)
t.end_fill()

for i in range(2000):
    t.penup() 
    t.goto(random.randint(-300,300),random.randint(-300,300))
    t.pendown()
    for j in range(5):
      t.fillcolor("white")
      t.begin_fill()
      t.forward(10)
      t.end_fill()
      t.left(144)



turtle.done()