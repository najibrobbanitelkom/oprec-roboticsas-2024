
def pertambahan (a,b):
    return a+b

def pengurangan (a,b):
    return a-b

def perkalian (a,b):
    return a*b

def pembagian (a,b):
    if b == 0:
        print("Penyebut tidak boleh nol, COba kembali")
    return a/b

def ulangi():
    ulang = int(input("Apakah anda ingin kembali ? (1 untuk ya): "))
    if ulang == 1:
        kalkulator_utama()
    else :
        print("Terimakasih")

def kalkulator_utama():
    print("============ KALKULATOR =============\n")
    print("1. Operasi Pertambahan\n")
    print("2. Operasi Pengurangan\n")
    print("3. Operasi Perkalian\n")
    print("4. Operasi Pembagian\n")

    choice = int(input("Masukkan pilihan operasi: "))
    print("\n")
    if choice in range(1,5):
        try :
            c = float(input("Masukkan angka 1 : " ))
            d = float(input("Masukkan angka 2 : "))
            if choice == 1:
                print("- Pertambahan")
                print(f"Hasil penjumlahan {c} + {d} adalah ", pertambahan(c,d))
                ulangi()
            elif choice == 2:
                print("- Pengurangan")
                print(f"Hasil pengurangan {c} - {d} adalah ", pengurangan(c,d))
                ulangi()
            elif choice == 3:
                print("- Perkalian")
                print(f"Hasil perkalian {c} x {d} adalah ", perkalian(c,d))
                ulangi()
            elif choice == 4:
                print("- Pembagian")
                print(f"Hasil pembagian {c} / {d} adalah ", pembagian(c,d))
                ulangi() 
        except ValueError:
            print("Maaf nilai angka yang dimasukkan tidak valid")
            kalkulator_utama()
    else :
        print("Maaf pilihan tidak ada dalam list")
        kalkulator_utama()

kalkulator_utama()

            




    

        