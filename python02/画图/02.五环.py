import turtle

turtle.width(10)

turtle.color("#0002fb")
turtle.circle(50)
# 画完抬笔
turtle.penup()
# 走
turtle.goto(130, 0)
turtle.pendown()
# 落
turtle.color("black")
turtle.circle(50)
turtle.penup()

turtle.goto(260, 0)
turtle.pendown()

turtle.color("red")
turtle.circle(50)
turtle.penup()

turtle.goto(60, -50)
turtle.pendown()

turtle.color("#fefd05")
turtle.circle(50)
turtle.penup()

turtle.goto(190, -50)
turtle.pendown()

turtle.color("#0bfbfa")
turtle.circle(50)
turtle.done()