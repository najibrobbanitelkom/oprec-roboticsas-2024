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

def get_lower_bgr():
    lower_blue = cv2.getTrackbarPos('LB', 'BGR Trackbars')
    lower_green = cv2.getTrackbarPos('LG', 'BGR Trackbars')
    lower_red = cv2.getTrackbarPos('LR', 'BGR Trackbars')
    return(lower_blue, lower_green, lower_red)

def get_upper_bgr():
    upper_blue= cv2.getTrackbarPos('UB', 'BGR Trackbars')
    upper_green = cv2.getTrackbarPos('UG', 'BGR Trackbars')
    upper_red = cv2.getTrackbarPos('UR', 'BGR Trackbars')
    return(upper_blue, upper_green, upper_red)

def main(video):
    while True:
        ret, frame = video.read()
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # low = np.load('/home/lina/Documents/Lynn/purple_low.npy')
        # high = np.load('/home/lina/Documents/Lynn/purple_high.npy')
        # low = (0, 0, 0)
        #low = (140, 111, 0)
        #low = (0, 69, 246)
        #high = (255, 255, 255)
        # high = (0, 0, 225)
        #high = (255, 255, 0)
        low = np.load('/home/lina/Documents/Lynn/ungu_bawah.npy')
        high = np.load('/home/lina/Documents/Lynn/ungu_atas.npy')
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
    init_trackbars() #panggil trackbar
    cam = cv2.VideoCapture(0)
    main(cam)