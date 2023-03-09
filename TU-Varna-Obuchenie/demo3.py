import turtle
turtle.clear()
turtle.bgcolor('blue')
turtle.pensize(10)
colors = ['yellow','brown','green','orange','red','pink']
turtle.setx(0)
turtle.sety(0)
for i in range(20):
    turtle.pencolor(colors[i % 6])
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.setpos(0,0)
    turtle.right(20)
turtle.done()