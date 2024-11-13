def shopping_list(b):
    belanjaan_kamu = {}

    for barang in b:
        if barang in belanjaan_kamu:
            belanjaan_kamu[barang] += 1  
        else:
            belanjaan_kamu[barang] = 1  
    
    print(belanjaan_kamu)

barang_list = []  

while True:
    b = input("Masukkan barang : ")

    if b == "selesai":
        break
    else:
        barang_list.append(b)  
shopping_list(barang_list) 
