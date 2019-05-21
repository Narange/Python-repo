import turtle

t = turtle.Turtle()

t.speed(10)

for i in range(20):
    t.forward(200)
    t.left(170)

t.color("green", "red")
t.begin_fill()

for i in range(20):
    t.forward(500)
    t.left(170)

t.end_fill()

turtle.done()
