import turtle

def draw_animated_circle(steps):
    hulk = turtle.Turtle()
    hulk.shape("arrow")
    hulk.color("green")

    for j in range (1, 360, 10):
        for i in range (0, 4):
            hulk.fd(steps)
            hulk.right(90)
        hulk.right(10)

def draw_circle(circle_rad):
    cap = turtle.Turtle()
    cap.shape("turtle")
    cap.color("blue")
    cap.circle(circle_rad)

def draw_triangle(steps):
    tony = turtle.Turtle(shape="classic")
    tony.color("white")
    for i in range (0, 3):
        tony.fd(steps)
        tony.right(120)


canvas = turtle.Screen()
canvas.bgcolor("red")
draw_animated_circle(100)
# draw_circle(100)
# draw_triangle(100)
canvas.exitonclick()
