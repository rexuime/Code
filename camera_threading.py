import time
import threading
import cv2
import serial
import numpy as np
from cubeClasses import cubeSide
from cubeClasses import sideSquare

'''
    Global matrix for current state of cube which will be modified by threads
    May need fine locking to prevent threads from accessing same value of matrix
    Would have to create a separate class/structure for a single square
    Each square would include its value and a lock
    Would then be a matrix of side objects that have square objects as the data
    lock = threading.Lock()
    with lock:
'''

# Global array side objects 
sides = []

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

    # sides list initialization
    global sides
    for i in range(6):
        sides.append(cubeSide(i))


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

    # modify squareSide objects
    return
    
# function for thread2 to do work for camera2/modify matrix
def p2():

    # modify squareSide objects
    return

# function to decode matrix into move for motors
def decode():

    # return data which will be used in sendData function
    return  

# function to auto scramble cube when chosen as scramble option
def scramble():

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

    # Add something to wait until we want to start 
    # When done solving, must come back and wait again

    # If manual scramble, use sendData
    # If auto scramble, use scramble function


    if isSolved:
        finish()

    readCube()