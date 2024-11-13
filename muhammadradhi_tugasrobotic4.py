def filter_even_numbers(numbers):
    x = []
    for number in numbers:
        if number % 2 == 0:
            x.append(number)
    return x

print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  
print(filter_even_numbers([7, 8, 10, 13]))       
