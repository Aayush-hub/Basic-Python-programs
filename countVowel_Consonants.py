#Python Program to Count Vowels and Consonants in a String

str1 = input("Enter a String : ")
vowels = 0
consonants = 0
str1.lower()

for i in str1:
    if(ord(i) == 65 or ord(i) == 69 or ord(i) == 73
       or ord(i) == 79 or ord(i) == 85
       or ord(i) == 97 or ord(i) == 101 or ord(i) == 105
       or ord(i) == 111 or ord(i) == 117):
        vowels = vowels + 1
    elif((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90)):
        consonants = consonants + 1
 
print("The number of vowels is ", vowels)
#Python Program to Count Vowels and Consonants in a String

print("The Nnumber of consonants is ", consonants)
