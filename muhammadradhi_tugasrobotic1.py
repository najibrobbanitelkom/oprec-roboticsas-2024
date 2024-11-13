def x(n):
    sum = 0
    for i in range( 1, n+1, 2):
        sum += i
    return sum
    
print(x(10))

#Fungsi pada sum_odd_numbers(10):

#start = 1: Memulai perulangan dari angka 1.
#stop = 10 + 1 = 11: Perulangan akan berhenti sebelum mencapai angka 11.
#step = 2: Setiap kali akan melompat dua angka.
#Jadi, angka yang akan dihasilkan dalam perulangan adalah: 1, 3, 5, 7, 9.