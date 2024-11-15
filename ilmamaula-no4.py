def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

print(filter_even_numbers([1, 2, 3, 4, 5, 6]))
print(filter_even_numbers([7, 8, 9, 10, 13]))