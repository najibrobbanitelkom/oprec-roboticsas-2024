def count_caracters(s):
    output = 1
    for char in huruf:
        if char == s:
            output = output + 1
    return output

huruf = input("huruf apa: ")
s = input("kalimat: ") 
print(count_caracters(s))
