import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(400,400)
sp = turtle.Turtle()

size = 0

while True:
    for i in range(5):
        sp.forward(size+1)
        sp.left(60)
        size = size-5
    size = size+1
