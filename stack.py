'''
Python program execute stack operation
Array-stacked operation
'''
import sys

# declaring empty stack
stack = []
op = 0 # For storing options and adding number
print("\n-------Array Stacked in Python-------\n")

# Stack operation begins here
while(True):
    print("Please enter the options:")
    print("1. Append  2. Pop  3. Display  4. Exit")
    op = int(input())
    if(op == 1):
        op = int(input("\nEnter the number to be appended: "))
        stack.append(op)
    elif(op == 2):
        print('\nElements poped from stack:') 
        print(stack.pop()) 
    elif(op == 3):
        print(stack)
    elif(op == 4):
        print("\nExiting...")
        break
    else:
        print("\nWrong input...Try again\n")
    
