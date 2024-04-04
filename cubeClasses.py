import threading
import numpy as np

class sideSquare:

    # Square has a lock to have safe resource sharing and data value
    def __init__(self):
        self.value = 'X'
        #self.lock = threading.Lock()

    # Setter for value
    def setVal(self, val):
        self.value = val

    # Getter for value
    def getVal(self):
        return self.value


class cubeSide:

    def __init__(self, num):
        self.matrix = np.full((3,3), sideSquare()) 
        #[[sideSquare() for i in range(3)] for j in range(3)]
        self.sideNumber = num

    """
    Need to figure out how to do this
    Is going to take what our camera sees and change the matrix to those values

    def setSide(self, input):
        # This needs to be changed
        for row in self.matrix:
            for j in row:
                j.setVal(input)
    """

    def printSide(self):
        print("Side " + str(self.sideNumber) + ":")
        for row in self.matrix:
            print("[",end="")
            for j in row:
                print(j.getVal(),end="")
            print("]")

"""

Code for testing

side = cubeSide(0)
side.printSide()

"""
