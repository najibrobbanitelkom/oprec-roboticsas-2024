def sum_odd_numbers(n):
    i = k = 0
    while i <= n:
        if(i % 2 == 0): 
            i += 1
            continue
        k += i
        i += 1
    print(k)

def main():
    num = int(input('input a number: '))
    sum_odd_numbers(num)

main()