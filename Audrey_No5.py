def shopping_list():
    shopping_list = {}

    while True:
        masukan = input("Masukan barang:")

        if masukan == "selesai":
            break

        if masukan in shopping_list:
            shopping_list[masukan] +=1
        else:
            shopping_list[masukan] = 1

    return print(shopping_list)

shopping_list()