def pengurangan(a, b):
    return a - b

def penjumlahan(a, b):
    return a + b

def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak bisa dibagi dengan nol"

def perkalian(a, b):
    return a * b

def kalkulator():
    a = float(input("Masukkan angka pertama: "))
    tanda = input("Masukkan operator (+, -, *, /): ")
    b = float(input("Masukkan angka kedua: "))

    if tanda == '+':
        hasil = penjumlahan(a, b)
    elif tanda == '-':
        hasil = pengurangan(a, b)
    elif tanda == '*':
        hasil = perkalian(a, b)
    elif tanda == '/':
        hasil = pembagian(a, b)
    else:
        hasil = "Operator tidak tersedia"

    print("Hasil: ", hasil)


kalkulator()
