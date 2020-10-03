number = int(input("Enter any number to check: "))
temp = number
sum = 0
while number > 0:
    last_digit = number % 10
    sum += last_digit
    number = number // 10

if temp % sum == 0:
    print (f'{temp} is Harshad Number')
else:
    print (f'{temp} is not Harshad Number')