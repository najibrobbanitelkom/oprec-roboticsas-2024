import cv2
import numpy as np
 
# Read image of planets
#planets = cv2.imread('planet.jpg')
cam = cv2.VideoCapture(0)

while True:

    ret, planets = cam.read()

# Convert image to grayscale
    gray_img = cv2.cvtColor(planets, cv2.COLOR_BGR2GRAY)
 
# Apply median blur to the grayscale image
    img = cv2.medianBlur(gray_img, 5)
 
# Convert blurred grayscale image back to BGR
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
 
# Detect circles in the image using HoughCircles
# Parameters:
# - img: the input image
# - cv2.HOUGH_GRADIENT: the detection method
# - 1: the inverse ratio of the accumulator resolution to the image resolution
# - 120: minimum distance between the centers of detected circles
# - param1: higher threshold for the Canny edge detector
# - param2: threshold for center detection
# - minRadius: minimum circle radius
# - maxRadius: maximum circle radius
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 120, param1=100, param2=30, minRadius=0, maxRadius=0)
    print(circles)
# Round circle parameters and convert to unsigned 16-bit integers
    circles = np.uint16(np.around(circles))
 
# Loop through each detected circle
    for i in circles[0, :]:
    # Draw the outer circle
    # Parameters:
    # - planets: the image to draw on
    # - (i[0], i[1]): the center coordinates of the circle
    # - i[2]: the radius of the circle
    # - (0, 255, 0): the color of the circle (green)
    # - 6: the thickness of the circle
        cv2.circle(planets, (i[0], i[1]), i[2], (0, 255, 0), 6)
 
    # Draw the center of the circle
    # Parameters:
    # - planets: the image to draw on
    # - (i[0], i[1]): the center coordinates of the circle
    # - 2: the radius of the center point
    # - (0, 0, 255): the color of the center point (red)
    # - 3: the thickness of the center point
        cv2.circle(planets, (i[0], i[1]), 2, (0, 0, 255), 3)
 
# Display image with detected circles
    cv2.imshow("HoughCircles", planets)
 
# Wait for key press indefinitely
    if cv2.waitKey(1) & 0xFF == ord('q') :
            break
 
# Close all OpenCV windows
