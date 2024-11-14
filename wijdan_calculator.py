import os

def penjumlahan(a, b):
    return a + b


def pengurangan(a, b):
    return a - b


def perkalian(a, b):
    return a*b

def pembagian(a, b):
    try:
        hasil = a/b
        return hasil
    except ZeroDivisionError:
        print("Bilangan pembagi tidak boleh nol!")

while True:
    os.system('cls||clear')
    print("Menu Kalkulator :\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian")
    pilih = int(input("Silahkan pilih :"))
    
    if pilih >= 1 and pilih < 6 :
        a = int(input("Masukkan a : "))
        b = int(input("Masukkan b : "))
        
        if pilih == 1:
            print(f"Hasil penjumlahan dari {a} dan {b} adalah : {penjumlahan(a,b)}")
        elif pilih == 2:
            print(f"Hasil pengurangan dari {a} dan {b} adalah : {pengurangan(a,b)}")
        elif pilih == 3:
            print(f"Hasil perkalian dari {a} dan {b} adalah : {perkalian(a,b)}")
        elif pilih == 4:
            print(f"Hasil pembagian dari {a} dan {b} adalah : {pembagian(a,b)}")
            
        print("Proses perhitungan berhasil! Coba lagi? Y/N")
        check = input()
        
        if check.lower == 'n':
            break
    else:
       print("pilihan salah! Coba lagi? Y/N")
       check = input()
       
       if check.lower == 'n':
           break