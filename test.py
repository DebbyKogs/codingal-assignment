import turtle


turtleVar = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=1000,height=800)
screen.bgcolor("black")
list = ["green","red","purple","pink","yellow","blue"]
turtleVar.pensize(3)
for i in range(250):
    turtleVar.color(list[i%len(list)])
    turtleVar.forward(i*10)
    turtleVar.left(170)
    turtleVar.circle(5)

turtle.done()