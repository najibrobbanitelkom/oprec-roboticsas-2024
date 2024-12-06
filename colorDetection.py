import cv2
import numpy as np

def callback():
    pass

def trackbar():
    cv2.namedWindow('BGR trackbar')
    cv2.createTrackbar('LB', 'BGR trackbar', 0, 255, callback)
    cv2.createTrackbar('LG', 'BGR trackbar', 0, 255, callback)
    cv2.createTrackbar('LR', 'BGR trackbar', 0, 255, callback)
    cv2.createTrackbar('UB', 'BGR trackbar', 255, 255, callback)
    cv2.createTrackbar('UG', 'BGR trackbar', 255, 255, callback)
    cv2.createTrackbar('UR', 'BGR trackbar', 255, 255, callback)

def getLowerHsv():
    lower_hue = cv2.getTrackbarPos('LB', 'BGR trackbar')
    lower_sue = cv2.getTrackbarPos('LG', 'BGR trackbar')
    lower_vue = cv2.getTrackbarPos('LR', 'BGR trackbar')
    return (lower_hue, lower_sue, lower_vue)

def getUpperHsv():
    upper_hue = cv2.getTrackbarPos('UB', 'BGR trackbar')
    upper_sue = cv2.getTrackbarPos('UG', 'BGR trackbar')
    upper_vue = cv2.getTrackbarPos('UR', 'BGR trackbar')
    return (upper_hue, upper_sue ,upper_vue)

def main(video):
    while True: 
        ret, frame = video.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # low = np.load('/Users/vscode/robotic_task/green_low.npy')
        # high = np.load('/Users/vscode/robotic_task/green_high.npy')
        lower = np.array(getLowerHsv())
        upper = np.array(getUpperHsv())

        thresh = cv2.inRange(frame, getLowerHsv(), getUpperHsv())
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))


        np.save('green_low.npy', lower)
        np.save('green_high.npy', upper)

        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        contour, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(f'contour, {contour}')
        if contour: 
            largest_contour = max(contour, key=cv2.contourArea)

            x,y,w,h = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame, (x,y), (w+x, h+y), (255, 0,0), 2)

            cv2.imshow('hsv', hsv)
            cv2.imshow('thres', thresh)
            cv2.imshow('frame', frame) 
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    trackbar()
    video=cv2.VideoCapture(0)
    main(video)
