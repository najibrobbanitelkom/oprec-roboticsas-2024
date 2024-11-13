def shopping_List():
    barang = {}
    while True:
        x = input("Masukkan barang: ")
        if x.lower() == "selesai":
            break
        if x in barang:
            barang[x] +=1
        else:
            barang[x] = 1
    return barang

print(shopping_List())