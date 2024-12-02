def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak terdefinisi"

def kalkulator():
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    
    while True:
        try:
            pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
            if pilihan in [1, 2, 3, 4]:
                break
            else:
                print("Pilihan tidak valid. Pilih 1, 2, 3 atau 4. ")
        except ValueError:
            print("Pilihan tidak valid. Masukkan angka.")

    a = int(input("Masukkan angka ke-1: "))
    b = int(input("Masukkan angka ke-2: "))

    operasi = {
        1: tambah,
        2: kurang,
        3: kali,
        4: bagi
    }
    
    hasil = operasi[pilihan](a, b)
    print(f"Hasil dari {a} {["tambah","kurang","kali","bagi"][pilihan-1]} {b} adalah {hasil}")

kalkulator()
