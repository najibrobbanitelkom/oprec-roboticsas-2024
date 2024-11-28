import cv2
import numpy as np
from cv2 import approxPolyDP

def getkontur(frame, framekontur):
    contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for kontur in contours:
        area = cv2.contourArea(kontur)
        if area > 500:
            cv2.drawContours(framekontur, [kontur], -1, (0, 0, 255), 2)
            peri = cv2.arcLength(kontur, True)
            approx = approxPolyDP(kontur, 0.02 * peri, True)
            korner = len(approx)

            x, y, w, h = cv2.boundingRect(approx)

            if korner == 3:
                benda = "segitiga"
            elif korner == 4:
                rasio = w / float(h)
                if  0.9<rasio<1.1:
                    benda = "persegi"
                else:
                    benda = "persegi panjang"
            elif korner == 8:
                benda = "lingkaran"
            else:
                benda = "Lainnya"

            cv2.rectangle(framekontur, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(framekontur, benda, (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)

def detect_color(frame, colors):
    for color_name, (low, high) in colors.items():
        thresh = cv2.inRange(frame, low, high)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, color_name, (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)

def main(video):
    colors = {
        "biru": (np.load('/home/zin/oprec-roboticsas-2024/blue_low.npy'), np.load('/home/zin/oprec-roboticsas-2024/blue_high.npy')),
        "merah": (np.load('/home/zin/oprec-roboticsas-2024/red_low.npy'), np.load('/home/zin/oprec-roboticsas-2024/red_high.npy')),
        "hijau": (np.load('/home/zin/oprec-roboticsas-2024/green_low.npy'), np.load('/home/zin/oprec-roboticsas-2024/green_high.npy')),
    }

    while True:
        ret, frame = video.read()
        if not ret:
            break

  
        detect_color(frame, colors)


        frameBlur = cv2.GaussianBlur(frame, (7, 7), 1) 
        frameCanny = cv2.Canny(frameBlur, 50, 70)


        getkontur(frameCanny, frame)

     
        cv2.imshow("Hasilnya cuy", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Tidak dapat membuka kamera.")
    else:
        main(camera)