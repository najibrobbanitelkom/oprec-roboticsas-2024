def shoppint_list():
    sample = dict()
    
    while True:
        a = input('Masukkan barang: ')
        if a == 'selesai': break
        if a in sample:
            sample[a] += 1
            continue
        sample[a] = 1
    print(sample)

shoppint_list()