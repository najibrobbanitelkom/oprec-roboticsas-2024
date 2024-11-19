def count_characters(s:str):
    charDict = {}
    for i in s:
        if i not in charDict:
            charDict[i] = 1
        else:
            charDict[i] += 1
    print(charDict)

count_characters("banana")
count_characters("hello")