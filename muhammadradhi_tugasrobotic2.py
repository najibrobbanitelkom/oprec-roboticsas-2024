def hitung_karakter(s):
    karakter_hitung = {}
    for char in s:
        if char in karakter_hitung:
            karakter_hitung[char] += 1
        else:
            karakter_hitung[char] = 1
    return karakter_hitung

print(hitung_karakter("banana")) 
print(hitung_karakter("hello"))   
