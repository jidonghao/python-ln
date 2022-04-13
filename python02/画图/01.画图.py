import turtle
turtle.pencolor("black")
turtle.fillcolor("black")
turtle.begin_fill()
while True:
    print(turtle.heading())
    if turtle.heading() / 90 % 2 == 0:
        turtle.forward(200)
    else:
        turtle.forward(100)
    turtle.right(90)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()
