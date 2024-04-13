import cv2
import numpy as np
from math import *

"""
---------
FUNCTIONS
---------
"""

# Function to get the average color of a specific region in the frame
def get_average_hsv(frame, top_left, bottom_right):
    region = frame[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    hsv_roi = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)
    average_hue = np.mean(hsv_roi[:, :, 0])
    average_saturation = np.mean(hsv_roi[:, :, 1])
    average_value = np.mean(hsv_roi[:, :, 2])
    
    return (floor(average_hue), floor(average_saturation), floor(average_value))


def hsv_to_color(hsv):
    # Unpack the HSV tuple
    h,s,v = hsv
    
    # Define HSV ranges
    red_rgb_ranges = [range(170, 180),range(50,255),range(100,255)]
    orange_rgb_ranges = [range(0,15),range(80,255),range(100,255)]
    yellow_rgb_ranges = [range(25,46),range(50,255),range(100,255)]
    green_rgb_ranges = [range(60,77),range(50,255),range(100,255)]
    blue_rgb_ranges = [range(86,115),range(50,255),range(100,255)]
    white_rgb_ranges = [range(0,70),range(0,70),range(100,255)]

    # Check if the RGB value falls within the defined color ranges
    if h in red_rgb_ranges[0] and s in red_rgb_ranges[1] and v in red_rgb_ranges[2]:
        return "Red"
    elif h in orange_rgb_ranges[0] and s in orange_rgb_ranges[1] and v in orange_rgb_ranges[2]:
        return "Orange"
    elif h in yellow_rgb_ranges[0] and s in yellow_rgb_ranges[1] and v in yellow_rgb_ranges[2]:
        return "Yellow"
    elif h in green_rgb_ranges[0] and s in green_rgb_ranges[1] and v in green_rgb_ranges[2]:
        return "Green"
    elif h in blue_rgb_ranges[0] and s in blue_rgb_ranges[1] and v in blue_rgb_ranges[2]:
        return "Blue"
    elif h in white_rgb_ranges[0] and s in white_rgb_ranges[1] and v in white_rgb_ranges[2]:
        return "White"
    else:
        return "Unknown"

if __name__ == "__main__":

    # Define the region of interest (ROI) coordinates
    top_left = (308, 228)  # Example top-left corner of the ROI
    bottom_right = (332, 252)  # Example bottom-right corner of the ROI
    x1,y1,x2,y2 = top_left[0], top_left[1], bottom_right[0],bottom_right[1]

    # Initialize the video capture object
    cap = cv2.VideoCapture(0)  # Use the default camera (usually index 0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        hsv = get_average_hsv(frame, top_left, bottom_right)
        color = hsv_to_color(hsv)
        #color = color_in_area(frame, top_left, bottom_right)
        #print("Color in the specified area:", color)

        cv2.rectangle(frame, top_left, bottom_right, (0,255,0), 1)
        text = color + ": (" + str(floor(hsv[0])) +", " + str(floor(hsv[1])) + ", " + str(floor(hsv[2])) + ")"
        cv2.putText(frame, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('Frame', frame)

        # Check for key press
        key = cv2.waitKey(1) & 0xFF
        #if key == ord('s'):
            # Get the average color of the ROI
            #print("Average HSV:", get_average_hsv(frame, top_left, bottom_right))
        if key == ord('q'):  # Press 'q' to exit
            break

    # Release the capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()