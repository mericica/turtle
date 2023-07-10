
from programs.program1 import programm1
from programs.program2 import *

def main():
    choice = str(input("1.Draw the following word: \n2. Add a new sign to the list"))
    assert(choice == "1" or choice == "2")
    if choice == "1":
        programm1()
    if choice == "2":
        programm2()


main()
