import turtle

def drawP(pkr):
    pkr.left(90)
    pkr.fd(100)
    for i in range(0, 3):
        pkr.rt(90)
        pkr.fd(50)

def drawK(pkr):
    pkr.pendown()
    pkr.rt(135)
    pkr.fd(71.17)
    pkr.lt(135)
    pkr.fd(50)
    pkr.penup()
    pkr.rt(180)
    pkr.fd(100)
    pkr.pendown()
    pkr.rt(180)
    pkr.fd(50)
    pkr.lt(135)
    pkr.fd(71)


def drawR(pkr):
    pkr.pendown()
    pkr.rt(180)
    pkr.fd(100)
    for i in range(0, 3):
        pkr.rt(90)
        pkr.fd(50)
    pkr.lt(135)
    pkr.fd(71)

def drawInitials():
    pkr = turtle.Turtle()
    pkr.shape("turtle")
    drawP(pkr)
    pkr.penup()
    pkr.rt(180)
    pkr.fd(150)
    pkr.rt(90)
    pkr.fd(50)
    drawK(pkr)
    pkr.penup()
    pkr.rt(45)
    pkr.fd(50)
    pkr.rt(90)
    pkr.fd(100)
    drawR(pkr)

canvas = turtle.Screen()
drawInitials()
canvas.exitonclick()