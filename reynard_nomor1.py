def sum_odd_numbers(angka):
    n = 1
    hasil = 0
    while n <= angka:
        if n % 2 != 0:
            print(n)
            hasil += n
        n += 1
    return hasil

angka = int(input("masukkan angka: "))
hasil = sum_odd_numbers(angka)
print("Total:", hasil)