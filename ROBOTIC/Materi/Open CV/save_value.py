import cv2
import numpy as np

def callback():
    pass

def init_trackbars():
    cv2.namedWindow('BGR Trackbars')
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
    return(lower_hue, lower_sat, lower_val)

def get_upper_hsv():
    upper_hue = cv2.getTrackbarPos('UB', 'BGR Trackbars')
    upper_sat = cv2.getTrackbarPos('UG', 'BGR Trackbars')
    upper_val = cv2.getTrackbarPos('UR', 'BGR Trackbars')
    return(upper_hue, upper_sat, upper_val)

def main(video):
    init_trackbars()
    while True:
        ret, frame = video.read()
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        low = get_lower_hsv()
        high = get_upper_hsv()
        thresh = cv2.inRange(frame, low, high) #membuat mask berdasarakan rentang waktu
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)  # melakukan operasi morfologi (open) untuk menghilangkan noise

        lower = np.array(low)
        higher = np.array(high)
        np.save('green_low.npy', lower)
        np.save('green_high.npy', higher)
        
        contour, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # menemukan contour pada gambar biner
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
