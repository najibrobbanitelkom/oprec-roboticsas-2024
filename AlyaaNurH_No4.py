def filter_even_numbers(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i, end=" ")

numbers = list(map(int, input("masukkan list bilangan bukat: ").split()))
filter_even_numbers(numbers)