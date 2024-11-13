def compare_numbers(a, b):
    if a > b:
        print("a lebih besar")
    elif a < b :
        print("b lebih besar")
    else:
        print("sama")

try:
    a = int(input("Masukkan angka a: "))
    b = int(input("Masukkan angka b: "))
    compare_numbers(a, b)
except  ValueError:
    print("Masukkan angka yang benar")