import cv2
import numpy as np

# def callback():
#     pass

# def init_trackbars():
#     #bikin window
#     cv2.namedWindow('HSV Trackbars')

#     #trackbars
#     cv2.createTrackbar('LB', 'BGR Trackbars', 0, 255, callback)
#     cv2.createTrackbar('LG', 'BGR Trackbars', 0, 255, callback)
#     cv2.createTrackbar('LR', 'BGR Trackbars', 0, 255, callback)

#     cv2.createTrackbar('UB', 'BGR Trackbars', 255, 255, callback)
#     cv2.createTrackbar('UG', 'BGR Trackbars', 255, 255, callback) 
#     cv2.createTrackbar('UR', 'BGR Trackbars', 255, 255, callback)

# def get_lower_hsv():
#     lower_hue = cv2.getTrackbarPos('LB', 'BGR Trackbars')
#     lower_sat = cv2.getTrackbarPos('LG', 'BGR Trackbars')
#     lower_val = cv2.getTrackbarPos('LR', 'BGR Trackbars')
#     return(lower_hue, lower_sat, lower_val)

# def get_upper_hsv():
#     upper_hue = cv2.getTrackbarPos('UB', 'BGR Trackbars')
#     upper_sat = cv2.getTrackbarPos('UG', 'BGR Trackbars')
#     upper_val = cv2.getTrackbarPos('UR', 'BGR Trackbars')
#     return(upper_hue, upper_sat, upper_val)

def main(video):
    # init_trackbars()
    while True:
        ret, frame = video.read()
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # low = np.load('C:\Users\Asus\Downloads\SEMESTER 1\ROBOTIC\openCamera\ila_lower.npy')
        # high = np.load('C:\Users\Asus\Downloads\SEMESTER 1\ROBOTIC\openCamera\ila_upper.npy')
        low = np.load('openCamera\ila_lower.npy')
        high = np.load('openCamera\ila_upper.npy')
        # low = get_lower_hsv()
        # high = get_upper_hsv()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv, low, high)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN,kernel)
        contour,_ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contour:
            largest_contour = max(contour, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame, (x, y), (w+x, h+y), (255, 0, 0), 2)

        # cv2.imshow('hsv', hsv)
        cv2.imshow('thresh', thresh)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__=='__main__':
    # init_trackbars() #panggil trackcbars
    cam = cv2.VideoCapture(0)
    main(cam)