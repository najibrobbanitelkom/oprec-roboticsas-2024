import cv2
import numpy as np

def callback():
    pass

def init_trackbars():
    #bikin windows
    cv2.namedWindow('HSV Trackbars')
    #track
    cv2.createTrackbar('LH', 'HSV Trackbar', 0, 255, callback)
    cv2.createTrackbar('LS', 'HSV Trackbar', 0, 255, callback)
    cv2.createTrackbar('LV', 'HSV Trackbar', 0, 255, callback)

    cv2.createTrackbar('UH', 'HSV Trackbar', 255, 255, callback)
    cv2.createTrackbar('US', 'HSV Trackbar', 255, 255, callback)
    cv2.createTrackbar('UV', 'HSV Trackbar', 255, 255, callback)

def get_lower_hsv():
    lower_hue = cv2.getTrackbarPos('LH', 'HSV Trackbar')
    lower_sat = cv2.getTrackbarPos('LS', 'HSV Trackbar')
    lower_val = cv2.getTrackbarPos('LV', 'HSV Trackbar')
    return(lower_hue)

def get_upper_hsv():
    upper_hue = cv2.getTrackbarPos ('UH', 'HSV Trackbars')
    upper_hue = cv2.getTrackbarPos ('US', 'HSV Trackbars')
    upper_hue = cv2.getTrackbarPos ('UV', 'HSV Trackbars')

def main(cam) :
    while True :
        ret, frame = cam.read()
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        high = np.load('/home/fizu/Downloads/Belajar Pyton/brown _High _npy.npy')
        low = np.load('/home/fizu/Downloads/Belajar Pyton/brown _low _npy.npy')
        thresh = cv2.inRange(frame, low, high)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        contour, _= cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print(f"contour{contour}")
        if contour:
            largest_contour = max(contour, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame, (x, y), (w+x, h+y), (255, 0, 0), 2)

        # cv2.imshow('hsv', thresh)
        cv2.imshow('thres', thresh)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    init_trackbars()
    cam = cv2.VideoCapture(0)
    main(cam)