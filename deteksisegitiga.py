import cv2

def getContour(frame, frameContour):
    contours, _ = cv2.findContours(frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:

            cv2.drawContours(frameContour, [cnt], -1, (0, 0, 255), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            korner = len(approx)
            print(korner)

            x, y, w, h = cv2.boundingRect(approx)

            if korner == 3:
                benda = "segi tiga"
            elif korner == 4:
                rasio = w / float(h)
                if 1.1 > rasio > 0.9:
                    benda = "persegi"
                else:
                    benda = "persegi panjang"
            else:
                benda = "lainnya"

            cv2.rectangle(frameContour, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frameContour, benda, (x + (w // 2) - 10, y + (h // 2) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

def main(video):
    while True:
        ret, frame = video.read()  

        if not ret:
            break  

        frameContour = frame.copy()

        frameBlur = cv2.GaussianBlur(frame, (7, 7), 1)
        frameCanny = cv2.Canny(frameBlur, 50, 70)

        getContour(frameCanny, frameContour)

        cv2.imshow("asli", frame)
        cv2.imshow("canny", frameCanny)
        cv2.imshow("HASIL", frameContour)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Kamera tidak dapat dibuka.")
    else:
        main(cam)
