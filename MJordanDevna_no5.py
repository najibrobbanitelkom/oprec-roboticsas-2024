totalbarang = {}
def shopping_list():
    while True:
       barang = input("Masukkan barang: ").lower()
       if barang == "selesai":
           break
       if barang not in totalbarang:
           totalbarang[barang] = 1
       else:
           totalbarang[barang] += 1
shopping_list()
print(totalbarang)

