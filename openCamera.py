import cv2

def main(cam):
    while True:
        ret, frame = cam.read()
        print(f"ret: \n\t{ret}\nframe:\n\t")
        cv2.imshow('nabil', frame)
        if cv2.waitKey(1) & 0xFF == ord ('h'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    camera = cv2.VideoCapture(0)
    main(camera)