import cv2
import numpy as np

def main(cam):
    while True:
        ret, frame = cam.read()
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # low = (146,111,0)
        # high = (255,255,0)
        # low = get_lower_bgr()
        # high = get_upper_bgr()

        low = np.load('/home/zin/oprec-roboticsas-2024/blue_low.npy')
        high = np.load('/home/zin/oprec-roboticsas-2024/blue_high.npy')

        thresh = cv2.inRange (frame,low,high)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN,kernel)


        contour,_ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contour:
            largest_contour = max(contour, key =cv2.contourArea)

            x,y,w,h =cv2.boundingRect(largest_contour)
            cv2.rectangle(frame,(x, y), (w+x, h+y), (255,0,0),2)
            cv2.putText(frame,"warna biru",(x+(w//2)-10, y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX, 0.7 , (0,0,0), 2 )

        # cv2.imshow("hsv", hsv)
        cv2.imshow("thresh", thresh)
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    # init_trackbars()
    camera = cv2.VideoCapture(0)
    main(camera)