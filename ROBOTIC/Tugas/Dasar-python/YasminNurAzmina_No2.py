def count_characters(s):
    hitung = {}
    for huruf in s:
        hitung[huruf] = hitung.get(huruf, 0) + 1
    return hitung

print(count_characters("banana"))
print(count_characters("hello"))
