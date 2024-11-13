#sum odd number (soal no 1)
def son (n):
    if n < 1 :
        return "ini bukan bilangan bulat positif"
    so = 0
    for i in range (1, n + 1):
        if i % 2 != 0 :
            so += i
    return so

n = int (input ("masukkan angka yang kamu cari : "))
print ("jumlah bilangan ganjil dari 1 hingga",n,"adalah", son (n))