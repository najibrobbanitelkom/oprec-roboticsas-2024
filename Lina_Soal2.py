def count_characthers(s):
    char_jumlah = {}
    for char in s:
        if char in char_jumlah:
            char_jumlah[char] += 1
        else:
            char_jumlah[char] = 1
    return print(char_jumlah)

count_characthers("banana")
count_characthers("hello")