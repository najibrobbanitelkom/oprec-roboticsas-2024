characters = {}

def count_characters(s):
    
    for x in s :
        if x in characters:
            characters[x] +=1
        else:
            characters[x] = 1 
        
user_input = input("Input your words : ");
count_characters(user_input)
print(characters)