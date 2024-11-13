def count_characters(s):

    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return print(char_count)

count_characters("banana")
count_characters("hello")