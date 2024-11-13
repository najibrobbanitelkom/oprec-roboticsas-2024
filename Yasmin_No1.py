def sum_odd_numbers(n):
    jumlah = 0
    for bilangan_ganjil in range(1, n+1, 2):
      jumlah += bilangan_ganjil
    print(jumlah)   
    
sum_odd_numbers(10)
sum_odd_numbers(7)

