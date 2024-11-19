itemDict = {}
def shopping_list():
    item = input("Masukkan barang: ")
    while item!="selesai":
        if item not in itemDict:
            itemDict[item] = 1
        else:
            itemDict[item] += 1
        item = input("Masukkan barang: ")

shopping_list()
print(itemDict)