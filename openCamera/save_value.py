import cv2
import numpy as np

def callback():
    pass

def init_trackbars():
    #bikin window
    cv2.namedWindow('BGR Trackbars')

    #trackbars
    cv2.createTrackbar('LB', 'BGR Trackbars', 0, 255, callback)
    cv2.createTrackbar('LG', 'BGR Trackbars', 0, 255, callback)
    cv2.createTrackbar('LR', 'BGR Trackbars', 0, 255, callback)

    cv2.createTrackbar('UB', 'BGR Trackbars', 255, 255, callback)
    cv2.createTrackbar('UG', 'BGR Trackbars', 255, 255, callback) 
    cv2.createTrackbar('UR', 'BGR Trackbars', 255, 255, callback)

def get_lower_hsv():
    lower_hue = cv2.getTrackbarPos('LB', 'BGR Trackbars')
    lower_sat = cv2.getTrackbarPos('LG', 'BGR Trackbars')
    lower_val = cv2.getTrackbarPos('LR', 'BGR Trackbars')
    return lower_hue, lower_sat, lower_val

def get_upper_hsv():
    upper_hue = cv2.getTrackbarPos('UB', 'BGR Trackbars')
    upper_sat = cv2.getTrackbarPos('UG', 'BGR Trackbars')
    upper_val = cv2.getTrackbarPos('UR', 'BGR Trackbars')
    return upper_hue, upper_sat, upper_val

def main(video):
    
    while True:
        ret, frame = video.read()
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # lower = np.load('openCamera\green_lowe.npy')
        # upper = np.load('openCamera\green_upper.npy')
        lower = get_lower_hsv()
        upper = get_upper_hsv()

        print(lower)
        print(upper)
        thresh = cv2.inRange(frame, lower, upper)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

        low = np.array((lower))
        high = np.array((upper))

        np.save('nila_lower.npy', low)
        np.save('nila_high.npy', high)

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
    cam = cv2.VideoCapture(0)
    init_trackbars()#panggil trackcbars
    main(cam)