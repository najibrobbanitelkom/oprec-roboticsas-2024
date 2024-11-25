import cv2
from cv2 import approxPolyDP

def deteksiWarna(h, s, v):
    if v < 50:
        return "Hitam"
    elif s < 50 and v > 200:
        return "Putih"
    elif s < 50:
        return "Abu-abu"
    elif h < 10 or h > 160:
        return "Merah"
    elif h < 25:
        return "Oranye"
    elif h < 35:
        return "Kuning"
    elif h < 85:
        return "Hijau"
    elif h < 100:
        return "Cyan"
    elif h < 130:
        return "Biru"
    elif h < 160:
        return "Ungu"
    elif h < 170:
        return "Pink"
    else:
        return "Tidak Terdefinisi"


def getContour(frame, hsv_frame, frameContour):
    contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(frameContour, cnt, -1, (121, 255, 221), 2)
            peri = cv2.arcLength(cnt, True)
            # epsilon = 0.01*cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            korner = len(approx)
            print(korner)

            x,y,w,h = cv2.boundingRect(approx)
            
            cx, cy = x + w // 2, y + h // 2
            pixel_object = hsv_frame[cy,cx]
            hue_value, saturation, value = pixel_object[0], pixel_object[1], pixel_object[2]

            pixel_bgr = frameContour[cy, cx]
            b, g, r = int(pixel_bgr[0]), int(pixel_bgr[1]), int(pixel_bgr[2])

            color = deteksiWarna(hue_value, saturation, value)

            if korner == 3:
                benda = "segitiga"
            elif korner == 4:
                rasio = w / float(h)
                if 1.1 > rasio > 0.9:
                    benda = "Persegi"
                else:
                    benda = "Persegi Panjang"
            elif korner >= 8: 
                benda = "Lingkaran"
            else: 
                benda = "Lainnya"

            cv2.circle(frameContour, (x+(w//2), y+(h//2)), 5, (0, 0, 255), 2)
            cv2.putText(frameContour,benda, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (45,102,45),2)
            cv2.putText(frameContour,color, (x+(w//2), y+(h//2)-50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (b-30,g-30,r-30),2)

def main(video):
    while True:
        _, frame = video.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        frameContour = frame.copy()

        frameBlur = cv2.GaussianBlur(frame, (7,7), 1)
        frameCanny = cv2.Canny(frameBlur, 50, 70)

        getContour(frameCanny, hsv_frame, frameContour)

        cv2.imshow("asli", frame)
        cv2.imshow("canny", frameCanny)
        # cv2.imshow("blur", frameBlur)
        cv2.imshow("HASIL", frameContour)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    # cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    main(cam)