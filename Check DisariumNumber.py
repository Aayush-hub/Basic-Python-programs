number = int(input("Enter any number to check: "))
length = len(str(number))
temp = number
result = 0

while number > 0:
    last_digit = number % 10
    result += last_digit**length
    number = number // 10
    length -= 1
    print(result)

if result == temp:
    print(f'{temp} is Disarium Number')
else:
     print(f'{temp} is not Disarium Number')
