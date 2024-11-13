def compare_numbers(a,b):
    if a > b:
        return "a lebih besar"
    elif b > a:
        return "b lebih besar"
    else:
        return "sama"
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
result = compare_numbers(a,b)
print(result)