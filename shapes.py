def square(turtle, color, size, x, y):
    turtle.up()  # не рисовать
    turtle.color(color)
    turtle.goto(x, y)  # перемещение по координатам

    turtle.down()  # начать рисовать
    for i in range(4):
        turtle.fd(size)
        turtle.rt(90)
    turtle.up()