def sum_odd_numbers(n):
    result = 0

    for i in range(1, n +1):
        if i % 2 != 0:
            result += i
    
    print(result) 

n =int(input("masukkan angka : "))
sum_odd_numbers(n)