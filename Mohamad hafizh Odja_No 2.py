# Count_Characters (soal no 2)
def cc(s):
    carihuruf = {}
    for karakter in s:
        if karakter in carihuruf:
            carihuruf[karakter] += 1
        else:
            carihuruf[karakter] = 1
    return carihuruf

inkata = str(input("Masukkan kata yang ingin kamu cari : "))
hasil = cc(inkata)
print(hasil)