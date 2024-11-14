def sum_odd_num(lim):
    if lim < 1:
        print("Numbers must be positive value and not zero!");
    else:
        sum = 0;
        for i in range(0, lim):
            if i%2 != 0 and i < lim:
                sum +=i
        return sum

user_input = int(input("Input your number here : "));          
print(f"The sum of the odd number is : {sum_odd_num(user_input)}");