buy_list = {}

value = 0

while True :
    x = input("Masukkan barang :")
    
    if x.lower() == 'selesai':
        break
    elif x in buy_list:
        buy_list[x] +=1
    else:
        buy_list[x] = 1
    
print(f"Barang yang dibeli beserta kuantitasnya : {buy_list}")

