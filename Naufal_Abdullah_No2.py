def count_characters(s):
    sample = dict()
    for item in s:
        if item in sample:
            sample[item] += 1
            continue
        sample[item] = 1
    print(sample)

def main():
    does = input('input a word: ')
    count_characters(does)
    
main()