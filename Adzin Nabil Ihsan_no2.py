def hitung_teks(kata):
    hasil_hitung = {}
    for char in kata.lower():  
        if char in hasil_hitung:
            hasil_hitung[char] += 1
        else:
            hasil_hitung[char] = 1
    return hasil_hitung

print(hitung_teks("banana"))
print(hitung_teks("hello"))
