import cv2

foto = cv2.imread('Foto/aku.jpeg')

cv2.imshow("foto mahal", foto)

cv2. waitKey(0)

cv2.destroyAllWindows()