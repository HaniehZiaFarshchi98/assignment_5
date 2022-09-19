
def isPalindrome (word):
    return word == word[::-1]

word = input("enter word:")
answer = isPalindrome (word)

if answer:
    print("is palindrome")
else:
    print("isn't palindrome")