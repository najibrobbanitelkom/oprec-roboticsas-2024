#compare Number (soal no 3)
def cn (a,b) :
    if a > b :
        return "a lebih besar"
    elif b > a :
        return "b lebih besar"
    else :
        return"sama"
a = int (input ("masukkan angka pertama : "))
b = int (input ("masukkan angka ke-dua : "))
print (cn(a,b))