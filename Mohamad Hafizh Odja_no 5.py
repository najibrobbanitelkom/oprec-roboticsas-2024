#Shoping List (soal no 5)
def sl():
    daftarbelanja = {}
    while True:
        belanjaan = input("Masukkan barang: ").strip().lower()
        if belanjaan == "selesai":
            break  
        if belanjaan in daftarbelanja:
            daftarbelanja[belanjaan] += 1
        else:
            daftarbelanja[belanjaan] = 1
    return daftarbelanja
hasil = sl()
print(hasil)