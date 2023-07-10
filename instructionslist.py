from wasdfg import *
instructionslist = []
def instructions():

    while True:
        input = str(input())
        if input == "w":
            W()
            instructionslist.append("w")
        if input == "a":
            A()
            instructionslist.append("a")
        if input == "s":
            S()
            instructionslist.append("s")
        if input == "d":
            D()
            instructionslist.append("d")
        if input == "f":
            F()
            instructionslist.append("f")
        if input == "g":
            G()
            instructionslist.append("g")
        if input == "":
            break
    return instructionslist

