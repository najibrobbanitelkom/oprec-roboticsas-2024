def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y


print("Select operation.")
print("1.tambah")
print("2.kurang")
print("3.kali")
print("4.bagi")

while True:
    C = input("pilih 1/2/3/4: ")
    if C in ('1', '2', '3', '4'):
        try:
            angka1 = int(input("bilangan pertama: "))
            angka2 = int(input("bilangan kedua: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if C == '1':
            print(angka1, "+", angka2, "=", tambah(angka1, angka2))

        elif C == '2':
            print(angka1, "-", angka2, "=", kurang(angka1, angka2))

        elif C == '3':
            print(angka1, "*", angka2, "=", kali(angka1, angka2))

        elif C == '4':
            print(angka1, "/", angka2, "=", bagi(angka1, angka2))

         
        
        K = input("Let's do next calculation? (yes/no): ")
        if K == "no":
          break
    else:
        print("Invalid Input")