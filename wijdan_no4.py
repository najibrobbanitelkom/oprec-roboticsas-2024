newNumber = []

def filter_even_numbers(nums):
    for check in nums:
        if check % 2 == 0:
            newNumber.append(check);
    return newNumber
            
x = []

limit = int(input("Input your number limit: "))
for i in range(limit):
    user_input = int(input("Input the value : "))
    x.append(user_input)
print(f"the filtered number : {filter_even_numbers(x)}")