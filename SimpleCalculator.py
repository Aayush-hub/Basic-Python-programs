
choice = int(input("Enter your choice:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5.Power\n"))
a = int(input("Enter any two number"))
b = int(input())
switcher = {
    1: f'The sum of {a} and {b} is {a + b}',
    2: f'The difference of {a} and {b} is {a - b}',
    3: f'The multiplication of {a} and {b} is {a * b}',
    4: f'The division of {a} and {b} is {a / b}',
    5: f'The result of {a} to the power {b} is {a ** b}',
}
print(switcher.get(choice, "Choice is Wrong!"))