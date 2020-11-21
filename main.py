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



done()