# Filter even number (soal no 4)
def efn(n):
    pemilih = [angka for angka in n if angka % 2 == 0]
    return pemilih
n1 = int(input("Masukkan angka pertama : "))
n2 = int(input("Masukkan angka kedua : "))
n3 = int(input("Masukkan angka ketiga : "))
n4 = int(input("Masukkan angka keempat : "))
n5 = int(input("Masukkan angka kelima : "))
n6 = int(input("Masukkan angka keenam : "))
n = [n1, n2, n3, n4, n5, n6]
print(efn(n))