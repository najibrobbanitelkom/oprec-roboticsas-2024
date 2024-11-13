def shopping_list():
    barang = {}
    while True:
        jenis = input("Masukkan barang: ")
        if jenis.lower() == "selesai":
            break
        if jenis in barang:
            barang[jenis] += 1
        else:
            barang[jenis] = 1
    return barang

hasil = shopping_list()
print("Output:", hasil)
