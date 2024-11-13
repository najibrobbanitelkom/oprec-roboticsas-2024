def sum_odd_numbers(number):
    i = 1
    result = 0
    while i <= number:
        if i % 2 != 0:
            print(i)
            result += i
        i += 1
    print("Hasil:", result)

number = int(input("masukkan angka: "))
sum_odd_numbers(number)