def tambah(x,y):
    print(x + y)

def kurang(x,y):
    print(x - y)

def kali(x,y):
    print(x * y)

def bagi(x, y):
    print(x / y)

print("========== KALKULATOR ==========\n")

print("ketik + untuk penambahan")
print("ketik - untuk pengurangan")
print("ketik / untuk pembagian")
print("ketik * untuk perkalian\n")

opsi = str(input("masukkan operasi yang diinginkan : \n"))

while True:
    try:
        if opsi == "+":
            x = int(input("masukkan nilai x = "))
            y = int(input("masukkan nilai y = "))

            tambah(x,y)
            break
        elif opsi == "-":
            x = int(input("masukkan nilai x = "))
            y = int(input("masukkan nilai y = "))

            kurang(x,y)
            break
        elif opsi == "/":
            x = int(input("masukkan nilai x = "))
            y = int(input("masukkan nilai y = "))
            if y == 0:
                print("gabisa broo membagi nol")

            bagi(x,y)
            break
        elif opsi == "*":
            x = int(input("masukkan nilai x = "))
            y = int(input("masukkan nilai y = "))
            
           

            kali(x,y)
            break
        else:
            print("input Invalid")
            
    except ValueError:
        print("Anda memasukkan selain dari operator diatas, harap masukkan ulang!!")