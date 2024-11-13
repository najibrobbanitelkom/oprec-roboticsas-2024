def sum_odd_numbers (n):
    jumlah = 0
    for x in range(1, n +1):
        if x % 2 != 0:
            jumlah += x
    return jumlah

print ("Output: ", sum_odd_numbers(10))

print ("Output: ", sum_odd_numbers(7))



           