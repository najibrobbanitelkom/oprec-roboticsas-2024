def count_characters(s):
    jumlah_karakter = {}  
    
    for char in s:
        if char in jumlah_karakter:
            jumlah_karakter[char] += 1  
        else:
            jumlah_karakter[char] = 1  
            
    print(jumlah_karakter)

s = str(input("Masukkan kata : "))
count_characters(s)
