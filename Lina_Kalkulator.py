def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "Pembagian tidak bisa menggunakan 0"

print("-----Kalkulator Sederhana-----")
print("------------------------------")

while True:
    print("\nPilih Operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan in ('1', '2', '3', '4'):
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))

            if pilihan == '1':
                hasil = penjumlahan(angka1, angka2)
                print("Hasil penjumlahan =", hasil)
            elif pilihan == '2':
                hasil = pengurangan(angka1, angka2)
                print("Hasil pengurangan =", hasil)
            elif pilihan == '3':
                hasil = perkalian(angka1, angka2)
                print("Hasil perkalian =", hasil)
            elif pilihan == '4':
                hasil = pembagian(angka1, angka2)
                print("Hasil pembagian =", hasil)
        except ValueError:
            print("Masukkan angka yang valid.")
    elif pilihan == '5':
        print("Anda keluar dari kalkulator.")
        break
    else:
        print("Pilihan tidak valid, silakan pilih kembali.")
