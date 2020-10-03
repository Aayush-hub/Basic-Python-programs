word = input("Enter any word ")
reversed_word = word[::-1] 

if word == reversed_word:
    print(f'{word} is palindrome')
else:
    print(f'{word} is not palindrome')