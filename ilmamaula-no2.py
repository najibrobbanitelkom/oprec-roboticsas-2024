def count_characters(s):
    characters_count = {}
    for char in s:
        if char in characters_count:
            characters_count[char] +=1
        else:
            characters_count[char] =1
    return characters_count

print(count_characters("banana"))
print(count_characters("hello"))