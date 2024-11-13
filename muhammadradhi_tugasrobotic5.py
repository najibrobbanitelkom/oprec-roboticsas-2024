def shopping_list():
    x = {}
    while True:
        y = input("Masukkan barang: ")
        if y.lower() == "selesai":
            break
        if y in x:
            x[y] += 1
        else:
            x[y] = 1
    return x

print(shopping_list())
