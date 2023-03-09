import turtle
turtle.setx(-300)
turtle.sety(0)
turtle.clear()
turtle.colormode(255)
turtle.bgcolor('blue')
turtle.pensize(5)
turtle.pencolor(240, 160, 80)


def fiveangle(sz):
    for i in range(5):
        turtle.forward(sz)
        turtle.left(72)

def square(sz2):
    for j in range(3):
        turtle.left(90)
        turtle.back(sz2)

for k in range(5):
    fiveangle(50)
    square(50)
    turtle.left(90)
    turtle.forward(50)
turtle.done()