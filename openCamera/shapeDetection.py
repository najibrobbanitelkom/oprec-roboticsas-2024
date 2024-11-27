import cv2
import numpy as np

def getContour(frame, frameContour, mask, color_label):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 300:
            cv2.drawContours(frameContour, cnt, -1, (0, 0, 255), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            corner = len(approx)
            print(corner)

            x, y, w, h = cv2.boundingRect(approx)

            if corner == 3:
                benda = "Segitiga"
            elif corner == 4:
                rasio = w / float(h)
                if 0.9 <= rasio <= 1.1:
                    benda = "Persegi"
                else:
                    benda = "Persegi Panjang"
            elif corner > 0:
                rasio = (4 * np.pi * area) / (peri ** 2)
                rasio_box = w / float(h)
                if 0.75 <= rasio <= 1.25:
                    benda = "Lingkaran"
                else:
                    benda = "Lainnya"
            else:
                benda = "Lainnya"

            cv2.rectangle(frameContour, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frameContour, f"{benda} ({color_label})", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)


def detectColor(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define HSV ranges for colors
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])
    lower_red1 = np.array([0, 150, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 150, 50])
    upper_red2 = np.array([180, 255, 255])
    lower_green = np.array([40, 70, 50])
    upper_green = np.array([80, 255, 255])

    # Create masks
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    red_mask = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    return blue_mask, red_mask, green_mask


def main(video):
    while True:
        ret, frame = video.read()
       
        frameContour = frame.copy()

        frameBlur = cv2.GaussianBlur(frame, (7, 7), 2)
        frameCanny = cv2.Canny(frameBlur, 50, 70) 

        # Detect colors
        blue_mask, red_mask, green_mask = detectColor(frame)

        # Process contours for each color
        getContour(frame, frameContour, blue_mask, "Biru")
        getContour(frame, frameContour, red_mask, "Merah")
        getContour(frame, frameContour, green_mask, "Hijau")

        # Display results
        cv2.imshow("Asli", frame)
        cv2.imshow("Canny", frameCanny)
        cv2.imshow("BLUR", frameBlur)
        cv2.imshow("HASIL", frameContour)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    main(cam)
