def filter_even_numbers(numbers):
    even_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
    return print(even_numbers)

filter_even_numbers([1, 2, 3, 4, 5, 6])
filter_even_numbers([7, 8, 9, 10])
