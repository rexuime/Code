import cv2
import numpy as np
from math import *

"""
---------
FUNCTIONS
---------
"""

# Function to get the average HSV of a specific region
# Takes in the region you want to get the average HSV of
# Returns a tuple of integer HSV values
def get_average_hsv(region):
    hsv_roi = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)
    average_hue = np.mean(hsv_roi[:, :, 0])
    average_saturation = np.mean(hsv_roi[:, :, 1])
    average_value = np.mean(hsv_roi[:, :, 2])
    
    return (floor(average_hue), floor(average_saturation), floor(average_value))


# Function to translate a tuple of HSV values to the color it represents
# Returns a char based on the color it translates to 
def hsv_to_color(hsv):
    # Unpack the HSV tuple
    h,s,v = hsv
    
    # Define HSV ranges
    # Don't pay attention to the variable names, these are HSV ranges
    red_rgb_ranges = [range(170, 180),range(50,255),range(100,255)]
    orange_rgb_ranges = [range(0,15),range(80,255),range(100,255)]
    yellow_rgb_ranges = [range(25,46),range(50,255),range(100,255)]
    green_rgb_ranges = [range(60,77),range(50,255),range(100,255)]
    blue_rgb_ranges = [range(86,115),range(50,255),range(100,255)]
    white_rgb_ranges = [range(0,70),range(0,70),range(100,255)]

    # Check if the RGB value falls within the defined color ranges
    #Red
    if h in red_rgb_ranges[0] and s in red_rgb_ranges[1] and v in red_rgb_ranges[2]:
        return 'F'
    #Orange
    elif h in orange_rgb_ranges[0] and s in orange_rgb_ranges[1] and v in orange_rgb_ranges[2]:
        return 'B'
    #Yellow
    elif h in yellow_rgb_ranges[0] and s in yellow_rgb_ranges[1] and v in yellow_rgb_ranges[2]:
        return 'U'
    #Green
    elif h in green_rgb_ranges[0] and s in green_rgb_ranges[1] and v in green_rgb_ranges[2]:
        return 'R'
    #Blue
    elif h in blue_rgb_ranges[0] and s in blue_rgb_ranges[1] and v in blue_rgb_ranges[2]:
        return 'L'
    #White
    elif h in white_rgb_ranges[0] and s in white_rgb_ranges[1] and v in white_rgb_ranges[2]:
        return 'D'
    else:
        return 'D'

if __name__ == "__main__":

    # Cube
    """cube = [[[(,),(,)],[(,),(,)],[(,),(,)]],
            [[(,),(,)],[(,),(,)],[(,),(,)]],
            [[(,),(,)],[(,),(,)],[(,),(,)]]]"""
    
    # The two matrices below, in there lowest lists, store [(xmin, ymin), (xmax, ymax), 'color of cublet']
    cam1 = [[[[],[],[]],
             [[],[],[]],
             [[],[],[]]],
             [[[],[],[]],
             [[],[],[]],
             [[],[],[]]]
             [[[],[],[]],
             [[],[],[]],
             [[],[],[]]]]
    
    cam2 = [[[[],[],[]],
             [[],[],[]],
             [[],[],[]]],
             [[[],[],[]],
             [[],[],[]],
             [[],[],[]]]
             [[[],[],[]],
             [[],[],[]],
             [[],[],[]]]]
    
    # List to store images
    img_list = []
    
    # List to store HSV values to get median and prevent outliers from taking over
    # To prevent a single bad image from ruining things
    h_list = []
    s_list = []
    v_list = []
    

    # Initialize the video capture object
    cap1 = cv2.VideoCapture(0)  # Use the default camera (usually index 0)
    cap2 = cv2.VideoCapture(1) # Unsure of what should go here for other camera

    # Take 10 pictures using cap1 and append them to image list
    for i in range(10):
        ret, frame = cap1.read()
        img_list.append(frame)

    # Iterate through matrix for cam1
    for side in cam1:
        for row in side:
            for cubelet in row:
                for i in img_list:

                    # Region of specific cubelet for cam1
                    region = frame[cubelet[0][1]:cubelet[1][1], cubelet[0][0], cubelet[1][0]]

                    # Append HSV values to their respective lists
                    h_list.append(get_average_hsv(region)[0])
                    s_list.append(get_average_hsv(region)[1])
                    v_list.append(get_average_hsv(region)[2])

                # Find median value in HSV lists to prevent outlier from causing errors
                h = np.median(h_list)
                s = np.median(s_list)
                v = np.median(v_list)
                hsv = (h,s,v)

                # Insert data into cubelet
                cubelet.append(hsv_to_color(hsv))

    # Empty lists
    h_list = []
    s_list = []
    v_list = []
    img_list = []

    # Take 10 pictures using cap2 and append them to image list
    for i in range(10):
        ret, frame = cap2.read()
        img_list.append(frame)

    # Iterate through matrix for cam2
    for side in cam2:
        for row in side:
            for cubelet in row:
                for i in img_list:

                    # Region of specific cubelet for cam1
                    region = frame[cubelet[0][1]:cubelet[1][1], cubelet[0][0], cubelet[1][0]]

                    # Append HSV values to their respective lists
                    h_list.append(get_average_hsv(region)[0])
                    s_list.append(get_average_hsv(region)[1])
                    v_list.append(get_average_hsv(region)[2])

                # Find median value in HSV lists to prevent outlier from causing errors
                h = np.median(h_list)
                s = np.median(s_list)
                v = np.median(v_list)
                hsv = (h,s,v)

                # Insert data into cubelet
                cubelet.append(hsv_to_color(hsv))


    # Merge all data cameras collected
    for i in cam2:
        cam1.append(i)

    # Output is a list of chars that are color coded to each cubelet
    output = []
    for side in cam1:
        for row in side:
            for cubelet in row:
                # Append color character data from cubelet to output
                output.append(cubelet[2])
