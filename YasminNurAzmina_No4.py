def filter_even_numbers(numbers):
    list_genap = []
    for a in numbers:
        if a % 2 == 0 :
            list_genap.append(a)
    print(list_genap)
    
filter_even_numbers([1, 2, 3, 4, 5, 6])
filter_even_numbers([7, 8, 10, 13])