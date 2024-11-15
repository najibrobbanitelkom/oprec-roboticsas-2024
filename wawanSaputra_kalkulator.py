def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error! Nilai kedua tidak boleh 0."
    return x / y

print("##===== Calculator in Python =====##")
print("Pilih operasi:")
print("[1] +Tambah   [2] -Kurang")
print("[3] *Kali     [4] /Bagi")
print("[5] Exit")

try:
    chose = 0
    while chose != 5:
        print("##================================##")
        chose = int(input("Pilihan : "))
        
        if chose==1 or chose==2 or chose==3 or chose==4:
            if chose == 1:
                print("Program (+)")
            if chose == 2:
                print("Program (-)")
            if chose == 3:
                print("Program (*)")
            if chose == 4:
                print("Program (/)")
                
            print("##================================##")
                
            num1 = float(input("Input angka pertama : "))
            num2 = float(input("Input angka kedua   : "))

            if chose == 1:
                print("Hasil               :", tambah(num1, num2))
            if chose == 2:
                print("Hasil               :", kurang(num1, num2))
            if chose == 3:
                print("Hasil               :", kali(num1, num2))
            if chose == 4:
                if num2 == 0:
                    print("Error! Nilai kedua tidak boleh 0.")
                    continue
                else:
                    print("Hasil               :", bagi(num1, num2))
        elif chose == 5:
            print("Keluar dari program.")
            break
        else:
            print("Error! Pilihan tidak valid.")
except ValueError:
    print("Error! Input tidak valid.")