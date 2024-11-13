def shopping_list():
    daftar = {}

    while True:
        barang = input("Masukkan nama barang: ")

        if barang == "selesai":
            break

        if barang in daftar:
            daftar[barang] += 1
        else:
            daftar[barang] = 1

    return daftar

# Contoh penggunaan
result = shopping_list()
print(result)