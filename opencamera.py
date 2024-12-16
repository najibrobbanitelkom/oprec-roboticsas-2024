import cv2

def main(cam):
    while True:
        ret, frame = cam.read()
        print(f"ret : \n\t{ret}\nfreme : \n\t")
        cv2.imshow('hasil', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    main(cam)
    #print(cam)