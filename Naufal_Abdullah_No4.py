def filter_even_numbers(numbers):
    new_list = []
    for item in numbers:
        if(item % 2 != 0): continue
        new_list.append(item)
    print(new_list)
def main():
    filter_even_numbers([1,2,3,4,5,6])
    filter_even_numbers([7,8,10,13])
main()