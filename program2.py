from instructionslist import *
def programm2():
    #stellt die neue zeichnen in ein Dokument 
    sign = input("Neues sign: ")
    instructions()
    with open("dict.txt") as f:
        new_dictionary = f.read()
        new_dictionary = eval(new_dictionary)
    if sign not in new_dictionary:
        new_dictionary[sign] = instructionslist
    f = open("dict.txt", "w")
    f.write(str(new_dictionary))
    f.close()
    
