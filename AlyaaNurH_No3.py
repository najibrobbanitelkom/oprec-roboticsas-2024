def compare_numbers(a, b):
    if a > b :
        print("a lebih besar")
    elif b > a:
        print("b lebih besar")
    else:
        print("sama")

a = int(input("masukkan a: "))
b = int(input("masukkan b: "))
compare_numbers(a, b)
