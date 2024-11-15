print("--------Kalkulator sederhana--------")
print("====================================")

def penjumlahan (a, b):
    return a + b

def pengurangan (a, b):
    return a - b

def perkalian (a, b):
    return a * b

def pembagian (a, b):
    if b != 0 :
        return a / b
    else :
        return "Tidak terdifinisi"
    
def kalkulator ():
    print("pilih salah satu operasi : ")
    print("penjumlahan (+)")
    print("pengurangan (-)")
    print("perkalian (*)")
    print("pembagian (/)")

    print("------------------------------------")

    option = (input("Pilih opsi (+, -, *, /): "))

    print("------------------------------------")

    angka1 = int(input('Masukkan angka pertama : '))
    angka2 = int(input('Masukkan angka kedua : '))

    print("------------------------------------")

    if option == '+' :
        print(f"hasilnya adalah : {penjumlahan(angka1, angka2)}")

    elif option == '-' :
        print(f"hasilnya adalah : {pengurangan(angka1, angka2)}")

    elif option == '*' :
        print(f"hasilnya adalah : {perkalian(angka1, angka2)}")

    elif option == '/' :
        print(f"hasilnya adalah : {pembagian(angka1, angka2)}")
    else :
        print(f"Silahkan pilih operasi yang tersedia! Try again!")
        

    print("====================================")

kalkulator()
