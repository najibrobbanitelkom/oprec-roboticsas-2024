import cv2
import numpy as np

def callback():
    pass

def init_trackbars():
    #HSV 
    # Bikin Window
    cv2.namedWindow('HSV Trackbar')
    cv2.createTrackbar('LH', 'HSV Trackbar', 0, 255, callback)
    cv2.createTrackbar('LS', 'HSV Trackbar', 0, 255, callback)
    cv2.createTrackbar('LV', 'HSV Trackbar', 0, 255, callback)

    cv2.createTrackbar('UH', 'HSV Trackbar', 255, 255, callback)
    cv2.createTrackbar('US', 'HSV Trackbar', 255, 255, callback)
    cv2.createTrackbar('UV', 'HSV Trackbar', 255, 255, callback)


def get_lower_hsv() :
    lower_hue= cv2.getTrackbarPos('LH', 'HSV Trackbar')
    lower_sat= cv2.getTrackbarPos('LS', 'HSV Trackbar')
    lower_val= cv2.getTrackbarPos('LV', 'HSV Trackbar')

    return (lower_hue, lower_sat, lower_val)

def get_upper_hsv() :
    upper_hue= cv2.getTrackbarPos('UH', 'HSV Trackbar')
    upper_sat= cv2.getTrackbarPos('US', 'HSV Trackbar')
    upper_val= cv2.getTrackbarPos('UV', 'HSV Trackbar')


    return (upper_hue, upper_sat, upper_val)


def main(video) :
    while True :
        ret, frame = video.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        low = get_lower_hsv()
        high = get_upper_hsv()
        thresh = cv2.inRange(hsv, low, high)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

        lower = np.array([low])
        upper = np.array([high])

        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        contour, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

        if contour :
            largest_contour = max(contour,key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(largest_contour)

            cv2.rectangle(frame, (x, y), (w+x, h+y), (255, 0, 0), 2)

        cv2.imshow('hsv', hsv)
        cv2.imshow('thres', thresh)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
if __name__ == '__main__' :
    cam = cv2.VideoCapture(0)
    init_trackbars()
    main(cam)

"""  
hue saturation value

yellow 
low = [171,176,0] atau [171,182,0]
high = [255,255,152]

blue
low = [0,0,214]
high = [27,45,255]

green
low = [0,207,14]
high = [184,255,255]

red
low = [241,0,0]
high = [255,184,112]


ini color sebelumnya (di shapeColorDetection):
    # Set range for red color and 
    # define mask 
    red_lower = np.array([136, 87, 111], np.uint8) 
    red_upper = np.array([180, 255, 255], np.uint8) 
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 

    # Set range for green color and 
    # define mask 
    green_lower = np.array([25, 52, 72], np.uint8) 
    green_upper = np.array([102, 255, 255], np.uint8) 
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 

    # Set range for blue color and 
    # define mask 
    blue_lower = np.array([94, 80, 2], np.uint8) 
    blue_upper = np.array([120, 255, 255], np.uint8) 
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 
"""