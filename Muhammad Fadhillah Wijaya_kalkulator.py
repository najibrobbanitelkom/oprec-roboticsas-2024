def tambah(a,b):
    a += b
    return a

def kurang(a,b):
    a -= b
    return a

def kali(a,b):
    a *= b
    return a

def bagi(a,b):
    a /= b
    return a

def pangkat(a,b):
    a **= b
    return a

def akar(a,b):
    a **= 1/b
    return a

def pilihOpsi():
    print("\nPilihan:")
    print("0. Clear")
    print("1. Tambah     (+)")
    print("2. Kurang     (-)")
    print("3. Kali       (x)")
    print("4. Bagi       (/)")
    print("5. Pangkat    (^)")
    print("6. Akar       (√)")
    print("7. Keluar/Selesai")
    pilihan = int(input("Pilih opsi: "))
    return pilihan

#main program
print("\n-== KALKULATOR SEDERHANA ==-")
pilihan = pilihOpsi()
if pilihan!=7:
    a = float(input("Masukkan bilangan awal: "))

while pilihan!=7:
    if pilihan == 1:
        b = float(input("Masukkan bilangan penambah: "))
        a = tambah(a,b)
    elif pilihan == 2:
        b = float(input("Masukkan bilangan pengurang: "))
        a = kurang(a,b)
    elif pilihan == 3:
        b = float(input("Masukkan bilangan pengali: "))
        a = kali(a,b)
    elif pilihan == 4:
        b = float(input("Masukkan bilangan pembagi: "))
        if b != 0:
            a = bagi(a,b)
        else:
            print("Penyebut/pembagi tidak boleh nol.\n")
    elif pilihan == 5:
        b = float(input("Masukkan nilai pangkat: "))
        a = pangkat(a,b)
    elif pilihan == 6:
        b = float(input("Masukkan nilai akar pangkat: "))
        if b >= 2:
            a = akar(a,b)
        else:
            print("Nilai akar pangkat harus >= 2.")
    elif pilihan == 0:
        a = 0
    else:
        print("Masukkan tidak valid.\n")
    print(f"\nHasil saat ini: {a}")
    pilihan = pilihOpsi()

print(f"\nHasil kalkulasi: {a}\n")
    