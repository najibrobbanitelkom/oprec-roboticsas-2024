import cv2
from cv2 import approxPolyDP

def getContour(frame, thresh, frameContour):
    contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
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
            #elif korner == 5: benda = "Segi lima"
            #elif korner == 6: benda = "Segi enam"
            #elif korner == 7: benda = "Segi tujuh"
            #elif korner == 8: benda = "Segi delapan"
            #elif korner <= 10000: benda = "Lingkaran"
            else: benda = "Lainnya"

            cv2.rectangle(frameContour, (x,y), (x+w, y+h), (255,0,0), 2)
            cv2.putText(frameContour, benda, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)


def main(video):
    while True:
        ret, frame = video.read()

        frameContour = frame.copy()
        frameBlur = cv2.GaussianBlur(frame, (7,7), 1)
        frameCanny = cv2.Canny(frameBlur, 50, 70)

        getContour(frameCanny, frameContour)

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