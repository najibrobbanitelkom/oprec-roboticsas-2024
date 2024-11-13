def shopping_list():
    barang_belanja = {}
    while True:
        barang = input("Masukkan barang: ")
        if barang == "selesai":
            break
        if barang in barang_belanja:
            barang_belanja[barang] += 1
        else:
            barang_belanja[barang] = 1
        return barang
    print(shopping_list)
shopping_list()
