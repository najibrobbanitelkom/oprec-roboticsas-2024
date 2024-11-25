import cv2
import numpy as np
from cv2 import approxPolyDP

def getContour(frame, frameContour):
    contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(frameContour, cnt, -1, (0, 0, 255), 2)
            peri = cv2.arcLength(cnt, True)
            approx = approxPolyDP(cnt, 0.02*peri, True)
            korner = len(approx)
            print(korner)

            x,y,w,h = cv2.boundingRect(approx)

            if korner == 3: benda = "Segi tiga"
            elif korner == 4:
                rasio = w / float(h)
                # if rasio > 0.9 and rasio < 1.1 : benda = "Persegi"
                # else : benda = "Persegi Panjang"
                if 1.1 > rasio > 0.9: benda = "Persegi"
                else: benda = "Persegi Panjang"
            elif korner == 5: benda = "Segi Lima"
            elif korner == 6: benda = "Segi Enam"
            elif len(approx) > 4 : benda = "Lingkaran"
            else: benda = "lainnya"

            mask = np.zeros(frameContour.shape[:2], dtype=np.uint8)
            cv2.drawContours(mask, [cnt], -1, 255, -1)
            mean_val = cv2.mean(frame, mask=mask)
            color = getColorName(mean_val)

            cv2.rectangle(frameContour, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frameContour, benda, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
            cv2.putText(frameContour, color, (x+(w//2)-10, y+(h//2)+10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)


def getColorName(mean_val):
    # Ambil nilai rata-rata B, G, dan R
    b, g, r = map(int, mean_val[:3])
    # Format nilai BGR menjadi string untuk ditampilkan
    return f"B: {b}, G: {g}, R: {r}"


def main(video):
    while True:
        ret, frame = video.read()

        frameContour = frame.copy()

        frameBlur = cv2.GaussianBlur(frame, (7,7),1)
        frameCany = cv2.Canny(frameBlur, 50, 70)

        getContour(frameCany, frameContour)

        cv2.imshow('Asli', frame)
        cv2.imshow('Canny', frameCany)
        # cv2.imshow('Blur', frameBlur)
        cv2.imshow('Hasil', frameContour)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    main(cam)