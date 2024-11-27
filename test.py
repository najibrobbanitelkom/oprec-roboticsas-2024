import cv2
import numpy as np

def callback():
    pass

def init_trackbars():
    cv2.namedWindow("bgr Trackbars")

    cv2.createTrackbar('LB', 'bgr Trackbars', 0, 255, callback)
    cv2.createTrackbar('LG', 'bgr Trackbars', 0, 255, callback)
    cv2.createTrackbar('LR', 'bgr Trackbars', 0, 255, callback)
    cv2.createTrackbar('UB', 'bgr Trackbars', 255, 255, callback)
    cv2.createTrackbar('UG', 'bgr Trackbars', 255, 255, callback)
    cv2.createTrackbar('UR', 'bgr Trackbars', 255, 255, callback)
    
def get_lower_bgr():
    lower_hue = cv2.getTrackbarPos('LB', 'bgr Trackbars')
    lower_sat = cv2.getTrackbarPos('LG', 'bgr Trackbars')
    lower_val = cv2.getTrackbarPos('LR', 'bgr Trackbars')
    return lower_hue,lower_val,lower_sat

def get_upper_bgr():
    upper_hue = cv2.getTrackbarPos('UB', 'bgr Trackbars')
    upper_sat = cv2.getTrackbarPos('UG', 'bgr Trackbars')
    upper_val = cv2.getTrackbarPos('UR', 'bgr Trackbars')
    return upper_hue,upper_sat,upper_val

def main(cam):
    while True:
        ret, frame = cam.read()
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # low = (146,111,0)
        # high = (255,255,0)
        # low = get_lower_bgr()
        # high = get_upper_bgr()

        low = np.load('/home/zin/oprec-roboticsas-2024/yellow_low.npy')
        high = np.load('/home/zin/oprec-roboticsas-2024/yellow_high.npy')
        print(low)
        print(high)

        thresh = cv2.inRange (frame,low,high)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN,kernel)


        contour,_ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contour:
            largest_contour = max(contour, key =cv2.contourArea)

            x,y,w,h =cv2.boundingRect(largest_contour)
            cv2.rectangle(frame,(x, y), (w+x, h+y), (255,0,0),2)

        # cv2.imshow("hsv", hsv)
        cv2.imshow("thresh", thresh)
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    # init_trackbars()
    camera = cv2.VideoCapture(0)
    main(camera)