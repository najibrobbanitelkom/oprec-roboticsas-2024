import cv2
from cv2 import approxPolyDP
import numpy as np


def getColor(hsv,frame,warna):
    #lowG = np.load('/home/fadhil/Documents/Materi_OpenCV/green_low.npy')  # Memuat batas bawah warna hijau dari file
    #highG = np.load('/home/fadhil/Documents/Materi_OpenCV/green_high.npy')  # Memuat batas atas warna hijau dari file
    if warna == "Hijau":
        low = np.array([8,168,0])
        high = np.array([149,255,255])
    elif warna == "Biru":
        pass
    elif warna == "Merah":
        pass
    elif warna == "Kuning":
        pass
    else:
        print("Warna tidak terseida.")
        return

    thresh = cv2.inRange(hsv, low, high)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    return thresh


def getContour(thresh, frameContour):
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(frameContour, cnt, -1, (0,0,255), 2)
            peri = cv2.arcLength(cnt, True)
            approx = approxPolyDP(cnt, 0.02*peri, True)
            korner = len(approx)
            print(korner)
            
            x,y,w,h = cv2.boundingRect(approx)

            if korner == 3: benda = "Segitiga"
            elif korner == 4:
                rasio = w/float(h)
                if 0.9 < rasio < 1.1: benda = "Persegi"
                else: benda = "Persegi Panjang"
            else: benda = "Lainnya"

            cv2.rectangle(frameContour, (x,y), (x+w, y+h), (255,0,0), 2)
            cv2.putText(frameContour, benda, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0), 2)


def main(video):
    while True:
        ret, frame = video.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Hijau
        thresh = getColor(hsv,frame, "Hijau")
        #contour, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        frameContour = frame.copy()
        frameBlur = cv2.GaussianBlur(thresh, (7,7), 1)
        frameCanny = cv2.Canny(frameBlur, 50, 70)

        getContour(frameCanny, frameContour)
        
        # Biru

        # Merah

        # Kuning

        """
        if contour :
            largest_contour = max(contour,key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(largest_contour)

            cv2.rectangle(frame, (x, y), (w+x, h+y), (255, 0, 0), 2)
        """
        #shape
        

        cv2.imshow("Asli", frame)
        cv2.imshow("Canny", frameCanny)
        #cv2.imshow("Blur", frameBlur)
        cv2.imshow("Hasil", frameContour)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    cam = cv2.VideoCapture(-1)
    main(cam)


"""         
            cv2.drawContours(imageFrame, contour, -1, (0,0,255), 2)
            peri = cv2.arcLength(contour, True)
            approx = approxPolyDP(contour, 0.02*peri, True)
            korner = len(approx)
            print(korner)
            
            x,y,w,h = cv2.boundingRect(approx)

            if korner == 3: benda = "Segitiga"
            elif korner == 4:
                rasio = w/float(h)
                if 0.9 < rasio < 1.1: benda = "Persegi"
                else: benda = "Persegi Panjang"
            #elif korner == 5: benda = "Segi lima"
            #elif korner == 6: benda = "Segi enam"
            #elif korner == 7: benda = "Segi tujuh"
            #elif korner == 8: benda = "Segi delapan"
            #elif korner <= 10000: benda = "Lingkaran"
            else: benda = "Lainnya"

            cv2.rectangle(imageFrame, (x,y), (x+w, y+h), (255,0,0), 2)
            cv2.putText(imageFrame, benda, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)
            """