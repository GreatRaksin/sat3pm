def square(turtle, color, size, x, y):
    turtle.up()  # не рисовать
    turtle.color(color)
    turtle.goto(x, y)  # перемещение по координатам

    turtle.down()  # начать рисовать
    for i in range(4):
        turtle.fd(size)
        turtle.rt(90)
    turtle.up()


def octagon(turtle, color, size, x, y):
    turtle.up()  # не рисовать
    turtle.color(color)
    turtle.goto(x, y)  # перемещение по координатам

    turtle.down()  # начать рисовать
    for i in range(8):
        turtle.fd(size)  # количество шагов
        turtle.lt(45)  # градус поворота
    turtle.up()


def spring(turtle, color, size, angle, x, y):
    turtle.up()  # не рисовать
    turtle.color(color)
    turtle.goto(x, y)  # перемещение по координатам

    turtle.down()
    for i in range(500):
        turtle.fd(size)
        turtle.lt(angle)
        size += 10
    turtle.up()
