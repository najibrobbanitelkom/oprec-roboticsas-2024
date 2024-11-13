def count_Characters(s):
    my_dict = {}
    for x in s:
        if x in my_dict:
            my_dict[x] += 1
        else :
            my_dict[x] = 1
    return my_dict

print(count_Characters("banana"))
print(count_Characters("Hello"))




