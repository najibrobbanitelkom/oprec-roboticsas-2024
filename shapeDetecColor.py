import cv2
import numpy as np
from cv2 import approxPolyDP

def getConotur(frame, frameB):
    contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(frameB, cnt, -1, (0, 0, 255), 2)
            peri = cv2.arcLength(cnt, True)
            approx = approxPolyDP(cnt, 0.02 * peri, True)
            korner = len(approx)
            print(f"Jumlah sudut: {korner}")
            
            x, y, w, h = cv2.boundingRect(approx)
            benda = "Tidak Teridentifikasi"
            
            if korner == 3:
                benda = "Segitiga"
            elif korner == 4:
                rasio = float(w) / h
                if 0.8 < rasio < 1.2:
                    benda = "Persegi"
                elif rasio > 1.2:
                    benda = "Persegi Panjang"
                elif rasio < 0.8:
                    benda = "Layang"
                else:
                    benda = "Trapesium atau Jajar Genjang"
            elif korner == 5:
                benda = "Segilima"
            elif korner == 6:
                benda = "Setengah Lingkaran"
            elif korner == 8:
                rasio = float(w) / h
                if 0.8 < rasio < 1.2:
                    benda = "Lingkaran"
                else:
                    benda = "Oval"
            elif korner == 9:
                benda = "Love"
            elif korner == 10:
                benda = "Bintang"
            elif korner == 12:
                benda = "Simbol Tambah"
            
            mask = frameB[y:y + h, x:x + w]
            hsv_mask = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
            
            lower_red = np.array([0, 120, 70])
            upper_red = np.array([10, 255, 255])

            lower_green = np.array([36, 50, 50])
            upper_green = np.array([89, 255, 255])

            lower_blue = np.array([94, 80, 2])
            upper_blue = np.array([126, 255, 255])
            
            red_mask = cv2.inRange(hsv_mask, lower_red, upper_red)
            green_mask = cv2.inRange(hsv_mask, lower_green, upper_green)
            blue_mask = cv2.inRange(hsv_mask, lower_blue, upper_blue)
            
            color = "Tidak Diketahui"
            if np.sum(red_mask) > 0:
                color = "Merah"
            if np.sum(green_mask) > 0:
                color = "Hijau"
            if np.sum(blue_mask) > 0:
                color = "Biru"
            
            label = f"{benda} {color}"
            cv2.rectangle(frameB, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frameB, label, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

def main(video):
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        frameB = frame.copy()
        frameBlur = cv2.GaussianBlur(frame, (7, 7), 1)
        frameCanny = cv2.Canny(frameBlur, 50, 70)
        
        getConotur(frameCanny, frameB)
        
        cv2.imshow("Asli", frame)
        cv2.imshow("Canny", frameCanny)
        cv2.imshow("Hasil", frameB)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    main(cam)
