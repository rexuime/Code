import time
import threading
import cv2
# pip install pyserial
import serial
from sideClass import cubeSide

# Global matrix for current state of cube which will be modified by threads
# May need fine locking to prevent threads from accessing same value of matrix
# lock = threading.Lock()
# with lock:
cubeMatrix = []

# Array for if we use class for sides
# sides = []

# Global variable to check if cube is solved
isSolved = False

# Global variable to wait until Arduino is done turning motors
arduinoIsRunning = False

# Global variable to hold all threads
threads = []

def setUp():

    # Thread initialization
    global threads
    t1 = threading.Thread(target = p1)
    threads.append(t1)
    t2 = threading.Thread(target = p2)
    threads.append(t2)

    # cubeMatrix initialization
    global cubeMatrix
    cubeMatrix = [[[0 for i in range(3)] for j in range(3)] for k in range(6)]

    # If we want to use a cubeSide class, the code for that is below
    """
    for i in range(6):
        side = cubeSide(i)
        sides.append(side)
    """

# function to start threads and read the cube/modify global matrix
def readCube():

    global threads
    # Start all the threads
    for thread in threads:
        thread.start()

    # Wait for all the threads to finish
    for thread in threads:
        thread.join()

# may want to implement a function to check? not sure yet

# function for thread1 to do work for camera1/modify matrix
def p1():

    # global "matrix"
    return
    
# function for thread2 to do work for camera2/modify matrix
def p2():

    # global "matrix"
    return

# function to decode matrix into move for motors
def decode():

    # return data which will be used in sendData function
    return  

# function to communicate with Arduino to turn motors 
# argument includes returned value from decode
def sendData():

    return

# function to finish things up when cube is solved
def finish():

    return


if __name__ == "__main__":

    setUp()

    if isSolved:
        finish()

    readCube()