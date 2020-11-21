from turtle import *
from shapes import *

t = Turtle()
t.shape('turtle')
t.shapesize(3, 3)
t.pen(fillcolor='lavender', pensize=5, speed=10, pencolor='lavender')

'''
fd(num) / forward(num)
bk(num) / backward(num)
lt(deg) / left(deg)
rt(deg) / right(deg)
'''
square(t, 'orange', 75, 50, 50)
square(t, 'red', 75, -50, -50)
square(t, 'yellow', 75, 150, 150)

for i in range(8):
    t.fd(50)  # количество шагов
    t.lt(45)  # градус поворота
    t.fd(50)

t.goto(100, -50)

done()