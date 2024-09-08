import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("white")
listOfColors = ["red","yellow","green","cyan","blue","magenta"]
for i in range(1000):
    t.color(listOfColors[i%6])
    t.forward(i%100)
    t.left(144)
turtle.done()