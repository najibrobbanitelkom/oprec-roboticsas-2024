def sum_odd_numbers(n):
    total = 0
    for i in range (1, n + 1):
        if i % 2 !=0:
            total += i
    return total
print(sum_odd_numbers(7))
print(sum_odd_numbers(10))