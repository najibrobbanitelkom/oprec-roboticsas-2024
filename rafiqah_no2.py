def count_characters(r):
    char_count = {}

    for char in r:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

word = (input("masukkan sebuah kata: "))
result = count_characters(word)
print(result)