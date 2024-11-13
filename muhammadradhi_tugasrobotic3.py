def x( a, b ):
    if a > b:
        return "a lebih besar daripada b"
    if a < b:
        return "a lebih kecil daripada b"
    if a == b:
        return "a sama dengan b"
    
print(x(5,4))
print(x(5,6))
print(x(5,5))