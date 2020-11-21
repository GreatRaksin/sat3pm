from turtle import *
from shapes import *

t = Turtle()

rectangle(t, 'black', 100, -50, 50)
t.goto(0, -30)
t.down()
t.color('red')
t.circle(35)
t.up()
t.goto(0, -140)
t.down()
t.color('green')
t.circle(35)
t.up()

minutes = int(input('Введите число: '))

if minutes % 2 == 0:
    print('Зеленый')
else:
    print('Красный')

done()