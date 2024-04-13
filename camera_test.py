import cv2

# define a video capture object 
vid = cv2.VideoCapture(0) 
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    # height 480, width 640
    # y = 480 pixels, x = 640 pixels
    ret, img = vid.read() 
  
    # Define the coordinates of the specific area
    x1, y1, x2, y2 = 0, 0, 640, 480

    # Crop the image to the specific area
    cropped_img = img[y1:y2, x1:x2]

    # Convert the image to HSV color space
    hsv_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2HSV)

    # Define the color range
    lower_range = (0, 50, 50) # lower range of red color in HSV
    upper_range = (10, 255, 255) # upper range of red color in HSV

    # Create a mask for the color
    mask = cv2.inRange(hsv_img, lower_range, upper_range)

    # Apply the mask to the image
    color_image = cv2.bitwise_and(cropped_img, cropped_img, mask=mask)

    # Display the color image
    cv2.imshow('Color Image', color_image)
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows()

