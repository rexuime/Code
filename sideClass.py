"""matrix = [[[0 for i in range(3)] for j in range(3)] for k in range(6)]
count = 0
count2 = 0
for i in range(len(matrix)):
    for k in matrix[i]:
        if count == 2:
            print(k)
            count = 0
        else:        
            print(k, end="    ")
            count += 1"""

class cubeSide:

    def __init__(self, num):
        self.matrix = [[0 for i in range(3)] for j in range(3)]
        self.sideNumber = num

    def setSide(self, input):
        self.matrix = input

    def printSide(self):
        print("Side " + str(self.sideNumber) + ":")
        print(self.matrix)

