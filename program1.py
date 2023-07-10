from signs import *
from wasdfg import *

def list_of_signs(char):

    f = open("dict.txt")
    for element in eval(f.read())[char]:
        if element == 'w':
            W()
        if element == 'a':
            A()
        if element == 's':
            S()
        if element == 'd':
            D()
        if element == 'f':
            F()
        if element == 'g':
            G()


def programm1():
    #zeichnet die definierte sign
    f = open("dict.txt")
    key = input("Zeichne dieses Wort: ")
    for char in key:
        if char in d:
            d[char]()
        else:
            list_of_signs(char)

    input()


