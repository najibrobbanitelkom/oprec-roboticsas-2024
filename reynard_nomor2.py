def count_characters(s):
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

kata = (input("masukkan kata: "))
hasil = count_characters(kata)
print(hasil)