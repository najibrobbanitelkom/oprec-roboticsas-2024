import cv2 
# import approxPolyDP
from cv2 import approxPolyDP

def getContour(frame, frameContour):
    contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # none = titik2 jadi garis. simpel = garis lurus, diambil ujung2nya doang
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(frameContour, cnt, -1, (100, 100, 100), 1)
            peri = cv2.arcLength(cnt, True)
            approx = approxPolyDP(cnt, 0.02*peri, True)
            korner = len(approx)
            print(korner)

            x, y, w, h = cv2.boundingRect(approx) # x = titik x | y = titik y | w = width | h = height
            # print("x = ", x, "y = ", y, "w = ", w, "h = ", h)
            if korner == 3: benda = "Segitiga"
            elif korner == 4: 
                rasio = w/float(h)
                # if rasio > 0.5 and rasio > 1.1: benda = "Persegi"
                if 1.1 > rasio > 0.5: benda = "Persegi"
                else: benda = "Persegi Panjang"
            elif 0.9 <= w / float(h) <= 1.1: benda = "Lingkaran"
            else : 
                benda = "Lainnya"

            if benda == "Segitiga":
                cv2.rectangle(frameContour, (x,y), (x+w, y+h), (255,0,0), 2)
            elif benda == "Persegi Panjang" or benda == "Persegi":
                cv2.rectangle(frameContour, (x,y), (x+w, y+h), (0, 0, 255), 2)
            elif benda == "Lingkaran":
                cv2.rectangle(frameContour, (x,y), (x+w, y+h), (255, 255, 255), 2)
            elif benda == "Lainnya" :
                cv2.rectangle(frameContour, (x,y), (x+w, y+h), (255,30,100), 2)
            # cv2.rectangle(frameContour, (x,y), (x+w, y+h), (255,0,0), 2)
            cv2.putText(frameContour, benda, (x+(w//3)-20, y+(h//3)-20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0), 2)

def main(video):
    while True:
        ret, frame = video.read()

        frameContour = frame.copy()

        frameBlur = cv2.GaussianBlur(frame, (7,7), 1)
        frameCanny = cv2.Canny(frameBlur, 50, 70)

        getContour(frameCanny, frameContour)

        cv2.imshow("ASLI", frame)
        cv2.imshow("CANNY", frameCanny)
        cv2.imshow("BLUR", frameBlur)
        cv2.imshow("HASIL", frameContour)

        if cv2.waitKey(1) & 0xFF == ord ('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    main(cam)

    # segitga, lingkaran, segiempat (persegi panjang dan persegi), lainnya
    # warna = BGR