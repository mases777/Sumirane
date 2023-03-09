import turtle
turtle.clear()
turtle.bgcolor('blue')
colors = ['yellow','green','red','white','brown','pink']
for i in range(12):
    turtle.pencolor(colors[i % 6])
    for j in range(6):
        turtle.forward(50)
        turtle.right(60)
    turtle.left(30)
turtle.done()