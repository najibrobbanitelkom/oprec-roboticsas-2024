def compare_numbers(a, b):
    if a > b:
        return "a lebih besar"
    elif a < b:
        return "b lebih besar"
    else:
        return "sama"

a = int(input("Masukkan angka 1: "))
b = int(input("Masukkan angka 2: "))
hasil = compare_numbers(a, b)
print(hasil)