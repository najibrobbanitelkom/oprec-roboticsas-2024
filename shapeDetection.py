import cv2
from cv2 import approxPolyDP

def getContour(frame, frameContour):
    contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for item in contours:
        area = cv2.contourArea(item)
        if area > 500:
            cv2.drawContours(frameContour, item, -1, (0, 0, 255), 2)
            parry = cv2.arcLength(item, True)
            approx = approxPolyDP(item, 0.02 * parry, True)
            korner = len(approx)

            x,y,w,h = cv2.boundingRect(approx)

            if korner == 4: benda = 'segitiga'
            else: benda = 'lainya'

            cv2.rectangle(frameContour, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frameContour, benda, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)

def main(video):
    while True:
        ret, frame = video.read()

        frameContour = frame.copy()

        frameBlur = cv2.GaussianBlur(frame, (7, 7), 1)

        frameCanny = cv2.Canny(frameBlur, 50, 70)

        getContour(frameCanny, frameContour)

        cv2.imshow('alsi', frame)
        cv2.imshow('canny', frameCanny)
        cv2.imshow('blur', frameBlur)
        cv2.imshow('hasil', frameContour)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    main(cam)