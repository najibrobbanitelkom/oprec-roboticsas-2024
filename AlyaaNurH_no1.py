def sum_odd_numbers(n):
    hasil = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            hasil = hasil + i
    return hasil

n = int(input())
print(sum_odd_numbers(n))