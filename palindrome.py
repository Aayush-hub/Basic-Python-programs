# Function to reverse the string using slicing
def CheckPalindrome(string):
    return string == string[::-1]

string = input("Please enter a string: ")
Check = CheckPalindrome(string)

if Check:
    print("It is palindrome")
else:
    print("No it is not palindrome")
