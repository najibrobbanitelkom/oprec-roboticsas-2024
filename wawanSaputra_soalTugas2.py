def count_characters(s):
    character_count = {}
    for char in s:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

try:
    s = input("Masukkan Kata : ")
    print(count_characters(s))
except ValueError:
    print("Input tidak valid")