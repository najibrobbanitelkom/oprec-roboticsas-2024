def kalkulator (a, op, b):
    if (op == '+'):
        return int(a) + int(b)
    elif (op == '-'):
        return int(a) - int(b)
    elif (op == '*'):
        return int(a) * int(b)
    elif (op == '/'):
        return int(a) / int(b)
    elif (op == '**'):
        return int(a) ** int(b)
    elif (op == '%'):
        return int(a) % int(b)
    elif (op == '//'):
        return int(a) // int(b)
    else:
        return False

a, op, b = input().split()
print(kalkulator(a, op, b))
print("apakah masih ingin menghitung? [y/n]")
ans = input()
print('')

while ans == 'y':
    a, op, b = input().split()
    print(kalkulator(a, op, b))
    print("apakah masih ingin menghitung? [y/n]")
    ans = input()
    print('')
    