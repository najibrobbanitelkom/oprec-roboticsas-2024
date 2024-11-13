iterasi = True

def penjumlahan(a,b):
    return a + b

def pengurangan(a,b):
    return a - b

def perkalian(a,b):
    return a * b

def pembagian(a,b):
    return a / b

while iterasi:
    print("\n\tKALKULATOR")
    print("-------------------------------")
    print("menu :")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("0. Stop")
    pilihan = int(input("Pilih Menu: "))

    if pilihan == 1:
        print("\nPenjumlahan")
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        hasil = penjumlahan(a,b)
        print(f"{a} + {b} = {hasil}")
    elif pilihan == 2:
        print("\nPengurangan")
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        hasil = pengurangan(a,b)
        print(f"{a} - {b} = {hasil}")
    elif pilihan == 3:
        print("\nPerkalian")
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        hasil = perkalian(a,b)
        print(f"{a} x {b} = {hasil}")
    elif pilihan == 4:
        print("\nPembagian")
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        hasil = pembagian(a,b)
        print(f"{a} / {b} = {hasil}")
    elif pilihan == 0:
        print("\nSelesai")
        iterasi = False
    else:
        print("\nMenu tidak tersedia")