#Python Program to Count Vowels and Consonants in a String

#taking user input (string)
str1 = input("Enter a String : ")

#initializing count variables for vowels & consonants (=0)
vowels = 0
consonants = 0
str1.lower()

#initializing list variables for vowels & consonants(=empty)
vowels_list=[]
consonants_list=[]

#checking each letter in string with its ascii value
for i in str1:
    if(ord(i) == 65 or ord(i) == 69 or ord(i) == 73
       or ord(i) == 79 or ord(i) == 85
       or ord(i) == 97 or ord(i) == 101 or ord(i) == 105
       or ord(i) == 111 or ord(i) == 117):
        #if vowel, then increment vowel variable by 1(vowels = vowels + 1)
        vowels = vowels + 1
        
        #add that vowel in list (if not already present in the list)
        if(i not in vowels_list):
          vowels_list.append(i)
    elif((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90)):
        #if consonant, then increment consonant variable by 1(consonants = consonants + 1)
        consonants = consonants + 1
        
        #add that consonant in list (if not already present in the list)
        if(i not in consonants_list):
          consonants_list.append(i)

#printing final sum of vowels & consonants
print("The number of vowels is ", vowels)
print("The number of consonants is ", consonants)

#printing seperate list of vowels & consonants
print("Vowels are", vowels_list)
print("Consonants are", consonants_list)
