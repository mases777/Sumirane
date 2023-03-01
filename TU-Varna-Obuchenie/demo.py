import turtle
#side = int(input("Length of size: "))
colors = ['yellow','green','red','white','brown','pink']
turtle.clear()
turtle.bgcolor('blue')
for i in range(200):
  turtle.pencolor(colors[i % 6])
  turtle.width(i / 100 + 1)
  turtle.forward(i)
  turtle.left(59)
turtle.done()