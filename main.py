from turtle import *

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
for i in range(8):
    t.fd(50)  # количество шагов
    t.lt(45)  # градус поворота
    t.fd(50)


done()