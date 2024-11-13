def penjumlahan_ganjil(n):
    jumlah = 0
    i = 1 
    while i <= n:
        if i % 2 != 0:
            jumlah += i
            print(i)
        i += 2
        return print(jumlah)
    print("Jumlah angka ganjil: ", jumlah)