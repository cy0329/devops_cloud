import turtle as t


def polygon(n):
    for i in range(n):
        t.fd(50)
        t.lt(360 / n)


def polygon2(n, a):
    for i in range(n):
        t.fd(a)
        t.lt(360 / n)


polygon(3)
polygon(5)

t.up()
t.back(25)
t.down()

polygon2(3, 100)
polygon2(5, 100)
