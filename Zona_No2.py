def count_characters(s):
        dictionary = {}
        for char in s:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
        return dictionary
print(count_characters("banana"))
print(count_characters("hello"))