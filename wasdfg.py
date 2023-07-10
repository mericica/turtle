"""
The following commands are used to draw new characters:
"""

import turtle
t = turtle.Pen()

def W():  #Moves forward with 1p pixels
    t.forward(10)

def S(): #Moves backwards
    t.backward(10)

def D(): #Makes in the right direction with 45 pixels
    t.right(45)

def A(): #Moves in the left direction
    t.left(45)

def F(): #picks the pen up
    t.up()

def G(): #puts the pen back down
    t.down()