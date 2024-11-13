def tambah(x,y):
    return x + y

def kurang(x,y):
    return x - y

def kali(x,y):
    return x * y

def bagi(x,y):
    if y == 0:
        return "Error! Nilai kedua tidak boleh 0."
    return x / y

print("##===== Calculator in Python =====##")
print("Pilih operasi:")
print("[1] Tambah   [2] Kurang")
print("[3] Kali     [4] Bagi")

chose=int(input("Pilihan : "))

print("##============ Input =============##")
try:
    num1 = float(input("Input angka pertama : "))
    num2 = float(input("Input angka Kedua   : "))

    if chose == 1:
        print("Operasi             : Tambah(+)")
        print("Hasil               :", tambah(num1,num2))
    elif chose == 2:
        print("Operasi             : Kurang(-)")
        print("Hasil               :", kurang(num1,num2))
    elif chose == 3:
        print("Operasi             : Kali(*)")
        print("Hasil               :", kali(num1,num2))
    elif chose == 4:
        print("Operasi             : Bagi(/)")
        if(num2 == 0):
            print(bagi())
        else:
            print("Hasil               :", bagi(num1,num2))
    else:
        print("Error! Pilihan tidak valid.")

except ValueError:
    print("Error! Input tidak valid.")

