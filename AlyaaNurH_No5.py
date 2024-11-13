def shopping_list():
    shopping_list = {}
    
    while True:
        beli = input("masukkan barang yang dibeli: ")

        if beli == "selesai":
            break
        if beli in shopping_list:
            shopping_list[beli] += 1
        else: 
            shopping_list[beli] = 1
    return print(shopping_list)

shopping_list()
