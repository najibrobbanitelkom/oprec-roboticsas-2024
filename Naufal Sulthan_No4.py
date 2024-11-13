def filter_even_numbers(numbers):
    number = []
    for x in numbers:
        if x % 2 == 0:
            number.append(x)
    return number
    

print(filter_even_numbers([1,2,3,4,5,6]))
print(filter_even_numbers([7,8,10,13]))