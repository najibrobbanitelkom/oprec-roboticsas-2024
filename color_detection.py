import cv2
import numpy as np

# Fungsi utama untuk memproses video
def main(video):
    while True:
        ret, frame = video.read()  # Membaca frame dari video/camera
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Mengubah frame dari BGR ke RGB
        low = np.load('green_low.npy')  # Memuat batas bawah warna hijau dari file
        high = np.load('green_high.npy')  # Memuat batas atas warna hijau dari file
        thresh = cv2.inRange(hsv, low, high)  # Membuat mask berdasarkan rentang warna hijau
        
        # Membuat kernel berbentuk elips dengan ukuran 5x5 untuk morfologi
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        
        # Melakukan operasi morfologi (open) untuk menghilangkan noise
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        
        # Menemukan kontur pada gambar biner
        contour, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contour:  # Mengecek apakah ada kontur yang ditemukan
            largest_contour = max(contour, key=cv2.contourArea)  # Memilih kontur terbesar berdasarkan area

            # Membuat kotak pembatas (bounding box) di sekitar kontur terbesar
            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame, (x, y), (w+x, h+y), (255, 0, 0), 2)  # Menggambar kotak di frame

        # Menampilkan hasil deteksi dalam beberapa jendela
        cv2.imshow('hsv', thresh)  # Menampilkan mask berdasarkan warna
        cv2.imshow('thres', thresh)  # Menampilkan hasil morfologi
        cv2.imshow('frame', frame)  # Menampilkan frame asli dengan kotak pembatas
        
        # Menunggu tombol 'q' untuk keluar dari program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Entry point dari program
if __name__ == '__main__':
    cam = cv2.VideoCapture(0)  # Membuka kamera default (index 0)
    main(cam)  # Memanggil fungsi utama
