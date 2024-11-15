def daftar_belanjaan():
    jumlah_barang = {}
    while True:
        barang = input("Masukkan barang: ")
        if barang.lower() == "selesai":
            break
        elif barang in jumlah_barang:
            jumlah_barang[barang] += 1
        else:
            jumlah_barang[barang] = 1
    return jumlah_barang

list_jumlah_barang = daftar_belanjaan()
print("Output:", list_jumlah_barang)
