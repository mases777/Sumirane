import random
import turtle
turtle.clear()
turtle.colormode(255)
turtle.bgcolor('blue')
turtle.pensize(5)
turtle.pencolor(240, 160, 80)

def triangle(sz):
    for i in range(3):
        turtle.forward(sz)
        turtle.left(120)

for j in range(100):
    m = random.randint(1, 255)
    n = random.randint(1, 255)
    p = random.randint(1, 255)
    #a = j*2 + 10
    b = 80 + j
    triangle(b)
    turtle.pencolor(m, n, p)
    turtle.right(5)
turtle.done()