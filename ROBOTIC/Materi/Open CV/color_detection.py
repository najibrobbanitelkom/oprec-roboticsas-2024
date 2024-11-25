import cv2
import numpy as np

def main(video):
    while True:
        ret, frame = video.read()
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # low = (0, 0, 0)
        # high = (0, 0, 225)
        # low = (140, 111, 0)
        # high = (255, 255, 0)
      
        # high = np.load('ROBOTIC/Materi/Open CV/green_high.npy') 
        # low = np.load('ROBOTIC/Materi/Open CV/green_lower.npy') 
        high = np.load('/home/yasmin/Documents/coba/green_high.npy') 
        low = np.load('/home/yasmin/Documents/coba/green_low.npy') 
        thresh = cv2.inRange(frame, low, high) #membuat mask berdasarakan rentang waktu
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel) # melakukan operasi morfologi (open) untuk menghilangkan noise

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

