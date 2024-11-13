def compare_numbers(a,b):
    if a > b:
        print("a lebih besar")
    elif b > a:
        print("b lebih besar")
    else:
        print("sama")

a = int(input("Masukkan nilai a : "))
b = int(input("Masukkan nilai b : "))
compare_numbers(a, b)