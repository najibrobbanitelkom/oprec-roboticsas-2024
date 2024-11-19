def filter_even_numbers(numbers: list):
    evenNum=[]
    for i in numbers:
        if i%2==0:
            evenNum.append(i)
    print(evenNum)

filter_even_numbers([1,2,3,4,5,6])
filter_even_numbers([7,8,10,13])