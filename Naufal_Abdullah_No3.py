def compare_numbers(a, b):
    if(a < b): return 'b lebih besar'
    return 'a lebih besar'

def main():
    a = input('input the first number: ')
    b = input('input the second number: ')
    print(compare_numbers(a, b))
    
main()