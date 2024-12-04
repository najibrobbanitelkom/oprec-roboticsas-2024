import cv2
from cv2 import approxPolyDP

def getContour(frame, frameContour):
    contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(frameContour, cnt, -1, (0, 0, 255), 2)
            ya = cv2.arcLength(cnt, True)
            approx = approxPolyDP(cnt, 0.02*ya, True)
            corner = len(approx)
            print(corner)

            x,y,w,h = cv2.boundingRect(approx)

            if corner == 3: benda = "Segitiga"
            elif corner == 4: 
                rasio = w / float(h)
                if rasio > 0.0 and rasio < 1.1: benda = "Persegi"
                else: benda = "Persegi Panjang"
            #elif tambah lingkaran sama gabung ke color detection
            else: benda = "Lainnya"

            cv2.rectangle(frameContour, (x,y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frameContour, benda, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0),2)

def main(video):
    while True:
        ret, frame = video.read()

        frameContour = frame.copy()

        frameBlur = cv2.GaussianBlur(frame, (7,7), 1)
        frameCanny = cv2.Canny(frameBlur, 50, 70)

        getContour(frameCanny, frameContour)

        cv2.imshow("Real", frame)
        cv2.imshow("Canny", frameCanny)
        cv2.imshow("Blur", frameBlur)
        cv2.imshow("Hasil", frameContour)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    main(cam)
