def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(calculate_factorial(5))
print(calculate_factorial(3))
print(calculate_factorial(0))
