import cv2
foto = cv2.imread('ROBOTIC/Materi/Open CV/src/foto.jpeg')

rgb = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(foto, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

cv2.imshow("Foto ", foto)
cv2.imshow("Foto RGB ", rgb)
cv2.imshow("Foto HSV ", hsv)
cv2.imshow("Foto Gray ", gray)

cv2.waitKey(0)
cv2.destroyAllWIndows()