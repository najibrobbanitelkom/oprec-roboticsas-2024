def shopping_list():
    daftar_belanja = {}

    while True:
        barang = input("Masukkan barang (ketik 'selesai' untuk mengakhiri): ")

        if barang.lower() == "selesai":
            break

        if barang in daftar_belanja:
            daftar_belanja[barang] += 1
        else:
            daftar_belanja[barang] = 1

    return daftar_belanja

# Contoh penggunaan
hasil = shopping_list()
print("Daftar Belanja:")
for barang, jumlah in hasil.items():
    print(f"{barang}: {jumlah}")