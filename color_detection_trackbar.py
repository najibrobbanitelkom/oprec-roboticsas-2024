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