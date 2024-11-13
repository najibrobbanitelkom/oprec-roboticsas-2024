def shopping_list():
    barang = ""
    jumlah = {}
    while barang != "selesai":
        barang = input("Masukkan barang :")
        
        if barang != "selesai":
            if barang in jumlah:
                jumlah[barang] += 1
            else:
                jumlah[barang] = 1
    
    return jumlah
       
print(shopping_list())
