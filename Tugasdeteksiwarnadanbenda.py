import cv2
import numpy as np
def getContour(frame, frameContour, color_name ):
    contours, _ = cv2.findContours(frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500 :

            cv2.drawContours (frameContour, [cnt], -1, (0, 0, 225), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            korner = len(approx)
            print(korner)

            x,y,w,h = cv2.boundingRect(approx)

            if korner == 3:
                benda = "segi tiga"
            if korner == 8:
                benda = "Lingkaran"
            elif korner == 4:
                rasio = w / float(h)
                if 1.1 > rasio > 0.9:
                    benda = "persegi"
                else:
                    benda = "persegi panjang"
            else:
                benda = "lainnya"

            cv2.rectangle(frameContour, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frameContour,f" {benda} {color_name}", (x + (w // 2) - 10, y + (h // 2) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
            
def get_lower_hsv() :
    lower_hue= cv2.getTrackbarPos('LB', 'BGR Trackbar')
    lower_sat= cv2.getTrackbarPos('LG', 'BGR Trackbar')
    lower_val= cv2.getTrackbarPos('LR', 'BGR Trackbar')

    return (lower_hue, lower_sat, lower_val)

def get_upper_hsv() :
    upper_hue= cv2.getTrackbarPos('UH', 'BGR Trackbar')
    upper_sat= cv2.getTrackbarPos('US', 'BGR Trackbar')
    upper_val= cv2.getTrackbarPos('UV', 'BGR Trackbar')


    return (upper_hue, upper_sat, upper_val)
            
def main(video):
    while True:
        ret, frame = video.read()  

        if not ret:
            break
        frameContour = frame.copy()
        frameBlur = cv2.GaussianBlur(frame, (7, 7), 1)
        frameCanny = cv2.Canny(frameBlur, 50, 70)

        low = np.load('/home/fizu/Downloads/Belajar Pyton/Red_low_npy.npy')
        high = np.load('/home/fizu/Downloads/Belajar Pyton/Red_High_npy.npy')
        color_name = "merah"
        thresh = cv2.inRange(frame, low, high)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        getContour(thresh, frameContour, color_name)

        cv2.imshow('thres', thresh)
        cv2.imshow('frame', frame)
        cv2.imshow("Hasil", frameContour)
        cv2.imshow("canny", frameCanny)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break

if __name__ == '__main__' :
    cam = cv2.VideoCapture(0)
    # init_trackbars()
    main(cam)