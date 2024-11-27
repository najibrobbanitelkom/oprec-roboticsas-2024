import cv2

foto = cv2.imread('openCamera\src\Gambar WhatsApp 2024-07-18 pukul 12.54.02_b50bb8f5.jpg')

rgb = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)
# hsv
# gray

cv2.imshow('KUPU KUPU', foto)
cv2.imshow("Foto RGB", rgb)
# hsv
# gray

cv2.waitKey(0)

cv2.destroyAllWindows()