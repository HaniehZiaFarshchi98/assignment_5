
word = input("enter word:") 
for i in range(len(word)):
    word = word.replace('e' , '?')
    word = word.replace('a' , '?')
    word = word.replace('y' , '?')
    word = word.replace('i' , '?')
    word = word.replace('o' , '?')
    word = word.replace('u' , '?')

print(word)
