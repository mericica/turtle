
from programs.program1 import programm1
from programs.program2 import *

def menu():
    input = str(input("1.Textnachritcht zeichnen \n2. Neues Wort hinzufugen"))
    assert(input == "1" or input == "2")
    if input == "1":
        programm1()
    if input == "2":
        programm2()


menu()



