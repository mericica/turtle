"""
All letter designs are defined here
"""
import turtle
turt = turtle.Turtle()


def A():
    turt.down()
    turt.left(90)
    turt.forward(60)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(60)
    turt.backward(30)
    turt.right(90)
    turt.forward(30)
    turt.left(90)
    turt.forward(30)
    turt.up()
    turt.left(90)
    turt.forward(40)


def B():
    turt.down()
    turt.left(90)
    turt.forward(60)
    turt.right(90)
    turt.forward(20)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(20)
    turt.backward(30)
    turt.left(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(30)
    turt.up()
    turt.left(180)
    turt.forward(40)


def C():
    turt.down()
    turt.forward(30)
    turt.backward(30)
    turt.left(90)
    turt.forward(60)
    turt.right(90)
    turt.forward(30)
    turt.up()
    turt.right(90)
    turt.forward(60)
    turt.left(90)
    turt.forward(10)


def D():
    turt.down()
    turt.left(90)
    turt.forward(60)
    turt.right(90)
    for i in range(30):
        turt.right(2)
        turt.forward(1)
    turt.right(30)
    turt.forward(45)
    turt.right(90)
    turt.forward(25)
    turt.up()
    turt.left(180)
    turt.forward(35)


def E():
    turt.down()
    turt.forward(30)
    turt.backward(30)
    turt.left(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(20)
    turt.backward(20)
    turt.left(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(30)
    turt.up()
    turt.right(90)
    turt.forward(60)
    turt.left(90)
    turt.forward(10)


def F():
    turt.down()
    turt.left(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(20)
    turt.backward(20)
    turt.left(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.up()
    turt.forward(60)
    turt.left(90)
    turt.forward(10)


def G():
    turt.down()
    x = turt.xcor()
    y = turt.ycor()
    turt.forward(30)
    turt.left(90)
    turt.forward(30)
    turt.left(90)
    turt.forward(15)
    turt.left(90)
    turt.forward(5)
    turt.up()
    turt.setposition(x, y)
    turt.left(180)
    turt.down()
    turt.forward(60)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(5)
    turt.up()
    turt.forward(55)
    turt.left(90)
    turt.forward(10)


def H():
    turt.down()
    turt.left(90)
    turt.forward(60)
    turt.backward(30)
    turt.right(90)
    turt.forward(30)
    turt.left(90)
    turt.forward(30)
    turt.backward(60)
    turt.right(90)
    turt.up()
    turt.forward(10)


def I():
    turt.up()
    turt.forward(10)
    turt.down()
    turt.left(90)
    turt.forward(60)
    turt.backward(60)
    turt.right(90)
    turt.up()
    turt.forward(10)


def J():
    turt.down()
    turt.left(90)
    turt.forward(15)
    turt.backward(15)
    turt.right(90)
    turt.forward(30)
    turt.left(90)
    turt.forward(60)
    turt.backward(60)
    turt.right(90)
    turt.up()
    turt.forward(10)


def K():
    turt.down()
    turt.left(90)
    turt.forward(60)
    turt.backward(30)
    turt.right(45)
    turt.forward(42.42640)
    turt.backward(42.42640)
    turt.right(90)
    turt.forward(42.42640)
    turt.left(45)
    turt.up()
    turt.forward(10)


def L():
    turt.down()
    turt.left(90)
    turt.forward(60)
    turt.backward(60)
    turt.right(90)
    turt.forward(30)
    turt.up()
    turt.forward(10)


def M():
    turt.down()
    turt.left(90)
    turt.forward(60)
    turt.right(90)
    turt.forward(15)
    turt.right(90)
    turt.forward(25)
    turt.backward(25)
    turt.left(90)
    turt.forward(15)
    turt.right(90)
    turt.forward(60)
    turt.left(90)
    turt.up()
    turt.forward(10)


def N():
    turt.down()
    turt.left(90)
    turt.forward(60)
    turt.right(160)
    turt.forward(64)
    turt.left(160)
    turt.forward(60)
    turt.backward(60)
    turt.right(90)
    turt.up()
    turt.forward(10)


def O():
    turt.down()
    turt.forward(30)
    turt.backward(30)
    turt.left(90)
    turt.forward(60)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(60)
    turt.left(90)
    turt.up()
    turt.forward(10)


def P():
    turt.down()
    turt.left(90)
    turt.forward(60)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(30)
    turt.backward(30)
    turt.left(90)
    turt.up()
    turt.forward(30)
    turt.left(90)
    turt.forward(10)


def Q():
    turt.down()
    turt.forward(30)
    turt.backward(30)
    turt.left(90)
    turt.forward(60)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(60)
    turt.left(45)
    turt.forward(5)
    turt.backward(20)
    turt.forward(15)
    turt.left(45)
    turt.up()
    turt.forward(10)


def R():
    turt.down()
    turt.left(90)
    turt.forward(60)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(30)
    turt.left(125)
    turt.forward(37)
    turt.left(55)
    turt.up()
    turt.forward(20)


def S():
    turt.down()
    turt.left(90)
    turt.forward(15)
    turt.backward(15)
    turt.right(90)
    turt.forward(30)
    turt.left(90)
    turt.forward(30)
    turt.left(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(15)
    turt.up()
    turt.forward(45)
    turt.left(90)
    turt.forward(10)


def T():
    turt.up()
    turt.forward(15)
    turt.down()
    turt.left(90)
    turt.forward(60)
    turt.right(90)
    turt.backward(15)
    turt.forward(30)
    turt.right(90)
    turt.up()
    turt.forward(60)
    turt.left(90)
    turt.forward(10)


def U():
    turt.down()
    turt.left(90)
    turt.forward(60)
    turt.backward(60)
    turt.right(90)
    turt.forward(30)
    turt.left(90)
    turt.forward(60)
    turt.backward(60)
    turt.up()
    turt.right(90)
    turt.forward(10)


def V():
    turt.up()
    turt.forward(15)
    turt.down()
    turt.left(75)
    turt.forward(60)
    turt.backward(60)
    turt.left(30)
    turt.forward(60)
    turt.backward(60)
    turt.right(105)
    turt.up()
    turt.forward(30)


def W():
    turt.up()
    turt.forward(10)
    turt.down()
    turt.left(75)
    turt.forward(30)
    turt.backward(30)
    turt.left(30)
    turt.forward(60)
    turt.backward(60)
    turt.right(105)
    turt.up()
    turt.forward(10)
    turt.down()
    turt.left(75)
    turt.forward(60)
    turt.backward(60)
    turt.left(30)
    turt.forward(30)
    turt.backward(30)
    turt.right(105)
    turt.up()
    turt.forward(30)


def X():
    turt.down()
    turt.left(60)
    turt.forward(60)
    turt.backward(30)
    turt.left(60)
    turt.forward(30)
    turt.backward(60)
    turt.right(120)
    turt.up()
    turt.forward(10)


def Y():
    turt.up()
    turt.forward(15)
    turt.down()
    turt.left(90)
    turt.forward(30)
    turt.left(30)
    turt.forward(30)
    turt.backward(30)
    turt.right(60)
    turt.forward(30)
    turt.backward(30)
    turt.left(30)
    turt.backward(30)
    turt.up()
    turt.right(90)
    turt.forward(30)


def Z():
    turt.down()
    turt.forward(30)
    turt.backward(30)
    turt.left(60)
    turt.forward(60)
    turt.left(120)
    turt.forward(30)
    turt.up()
    turt.backward(30)
    turt.left(90)
    turt.forward(55)
    turt.left(90)
    turt.forward(10)


def frage():
    turt.up()
    turt.left(90)
    turt.forward(40)
    turt.down()
    turt.forward(20)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(15)
    turt.left(90)
    turt.forward(20)
    turt.up()
    turt.forward(5)
    turt.down()
    turt.forward(5)
    turt.up()
    turt.left(90)
    turt.forward(25)


def ausrufe():
    turt.up()
    turt.forward(15)
    turt.left(90)
    turt.down()
    turt.forward(5)
    turt.up()
    turt.forward(5)
    turt.down()
    turt.forward(50)
    turt.up()
    turt.backward(60)
    turt.right(90)
    turt.forward(20)


def punkt():
    turt.down()
    for i in range(4):
        turt.forward(3)
        turt.left(90)
    turt.up()
    turt.forward(20)


def spatiu():
    turt.up()
    turt.forward(30)




d = {"A" : A, "B": B, "C" : C, "D" : D, "E" : E, "F" : F, "G": G, "H":H, "I": I, "J": J, "K": K, "L":L, "M":M, "N":N, "O":O, "P":P, "Q": Q, "R":R,
     "S": S, "T":T, "U": U, "V": V, "W": W, "X": X, "Y": Y, "Z": Z, '.': punkt, '?': frage, '!': ausrufe, ' ': spatiu}


def dictionar(input):
    return input