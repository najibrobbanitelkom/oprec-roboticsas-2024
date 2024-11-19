total = {}
def shopping_list():
    while True:
       barang = input("Masukkan barang: ").lower()
       if barang == "selesai":
           break
       if barang not in total:
           total[barang] = 1
       else:
           total[barang] += 1
shopping_list()
print(total)