def jumlahkan_ganjil(n):
    if n <= 0:
        return "harus positif"
    
    jumlah_total_ganjil = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            jumlah_total_ganjil += i
    
    return jumlah_total_ganjil


print(jumlahkan_ganjil(10))
print(jumlahkan_ganjil(7))