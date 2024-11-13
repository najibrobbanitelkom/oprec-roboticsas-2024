def filter_even_numbers(nl):
    genap = []
    for i in nl:
        if i % 2 == 0:
            genap.append(i)
    print(genap)

try:
    n = input("Masukkan beberapa angka (pisahkan dengan spasi): ")
    nl = []
    for num in n.split():
        nl.append(int(num))
except ValueError:
    print("Maaf, input tidak valid")
else:
    filter_even_numbers(nl)
