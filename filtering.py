import cv2

def main(cam):
    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.imshow("frame gray", gray)
        cv2.imshow("frame hsv", hsv)
        cv2.imshow("frame rgb", rgb)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    camera = cv2.VideoCapture(0)
    main(camera)