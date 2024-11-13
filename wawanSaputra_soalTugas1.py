def sum_odd_numbers(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:  
            total += i
    return total

try:
    n = int(input("Masukkan angka : "))
    if n > 0:
        print("Jumlah semua bilangan ganjil dari 1 hingga", n, "adalah:", sum_odd_numbers(n))
    else:
        print("Masukkan bilangan bulat positif.")
except ValueError:
    print("Masukkan angka yang valid.")