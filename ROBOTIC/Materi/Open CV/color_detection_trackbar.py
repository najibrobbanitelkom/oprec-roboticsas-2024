import cv2
import numpy as np

def callback():
    pass

def init_trackbars():
    cv2.namedWindow('HSV Trackbars')
    cv2.createTrackbar('LH', 'HSV Trackbars', 0, 255, callback)
    cv2.createTrackbar('LS', 'HSV Trackbars', 0, 255, callback)
    cv2.createTrackbar('LV', 'HSV Trackbars', 0, 255, callback)

    cv2.createTrackbar('UH', 'HSV Trackbars', 255, 255, callback)
    cv2.createTrackbar('US', 'HSV Trackbars', 255, 255, callback)
    cv2.createTrackbar('UV', 'HSV Trackbars', 255, 255, callback)
   
def get_lower_hsv():
    lower_hue = cv2.getTrackbarPos('LH', 'HSV Trackbars')
    lower_sat = cv2.getTrackbarPos('LS', 'HSV Trackbars')
    lower_val = cv2.getTrackbarPos('LV', 'HSV Trackbars')
    return(lower_hue, lower_sat, lower_val)

def get_upper_hsv():
    upper_hue = cv2.getTrackbarPos('UH', 'HSV Trackbars')
    upper_sat = cv2.getTrackbarPos('US', 'HSV Trackbars')
    upper_val = cv2.getTrackbarPos('UV', 'HSV Trackbars')
    return(upper_hue, upper_sat, upper_val)

def main(video):
    init_trackbars()
    while True:
        ret, frame = video.read()
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # low = (0, 0, 0)
        # high = (0, 0, 225)
        # low = (140, 111, 0) --
        # high = (255, 255, 0)--
        low = get_lower_hsv()
        high = get_upper_hsv()
        thresh = cv2.inRange(frame, low, high) #membuat mask berdasarakan rentang waktu

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        # melakukan operasi morfologi (open) untuk menghilangkan noise
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        # menemukan contour pada gambar biner
        contour, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(f"contour {contour}")
        if contour: #mengecek
            largest_contour = max(contour, key=cv2.contourArea)

            # membuat kotak
            x, y, w, h = cv2.boundingRect(largest_contour) 
            cv2.rectangle(frame, (x, y), (w+x, h+y), (255, 0, 0), 2) # menggambar kotak di frame

        # cv2.imshow("hsv", thresh) #menampilkan mask berdasarkan warna
        cv2.imshow("thresh", thresh) # menampilkan hasil mierfologi
        cv2.imshow("frame", frame) # menampilkan frame asli dengan kotak pembatas

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    main(cam)
  
#   PR = jingga
