#program kalkulator coyyyyyyyyy

def pertambahan():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    c = a + b
    print("Hasil pertambahan:",c)

def pengurangan():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    c = a - b
    print(f"Hasil pengurangan: {c}")

def perkalian():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    c = a * b
    print(f"Hasil perkalian: {c}")

def pembagian():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    c = a / b
    print(f"Hasil pembagian: {c}")

def main():
    print("Selamat datang di program kalkulator")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar Program")

    while True:
        x = int(input("Pilih opsi: "))
        
        if x == 1:
            pertambahan()
        elif x == 2:
            pengurangan()
        elif x == 3:
            perkalian()
        elif x == 4:
            pembagian()
        elif x == 5:
            print("Keluar Program...")
            break
        else:
            print("Opsi tidak ditemukan, coba lagi.")

if __name__ == "__main__":
    main()

