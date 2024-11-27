import cv2
from cv2 import approxPolyDP

def getkontur(frame,framekontur):
    contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for kontur in contours:
        area = cv2.contourArea(kontur)
        if area>500:
            cv2.drawContours(framekontur, kontur, -1, (0,0,255),2)
            peri = cv2.arcLength(kontur, True)
            approx = approxPolyDP(kontur, 0.02*peri,True)
            korner = len(approx)
            print(korner)

            x,y,w,h = cv2.boundingRect(approx)

            if korner == 3 : 
                benda = "segitiga"
            elif korner == 4 : 
                rasio = w/float(h)
                if  0.9>rasio>1.1:
                    benda = "persegi"
                else:
                    benda = "persegi panjang"
            elif korner > 10 :
                benda = "lingkaran"
            else : 
                benda = "Lainnya"
            cv2.rectangle(framekontur, (x,y), (x+w,y+h), (255,0,0),2)
            cv2.putText(framekontur, benda, (x+(w//2)-10, y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX, 0.7 , (0,0,0), 2 )

def main(video):
    while True:
        ret, frame = video.read()

        framekontur = frame.copy()
        frameBlur = cv2.GaussianBlur(frame, (7,7),1)
        frameCanny = cv2.Canny(frameBlur,50,70)

        getkontur(frameCanny, framekontur)

        cv2.imshow("ini frame",frame)
        cv2.imshow("frame canny", frameCanny)
        cv2.imshow("frame blur",frameBlur)
        cv2.imshow("Hasil brok", framekontur)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    camera = cv2.VideoCapture(0)
    main(camera)