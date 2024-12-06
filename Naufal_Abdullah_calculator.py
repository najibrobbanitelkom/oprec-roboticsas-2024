def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

def deside(types, a, b):
    match types:
        case 1: return addition(a, b)
        case 2: return subtraction(a, b)
        case 3: return multiplication(a, b)
        case 4: return division(a, b)

def play():
    calculator = int(input('choose a number below to do a math: \n 1: add \n 2: subtract \n 3: multiplication \n 4: division \n '))
    a = int(input('input first number: '))
    b = int(input('input second number: '))
    print(deside(calculator, a, b))

play()