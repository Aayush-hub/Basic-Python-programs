'''
Python program execute stack operation
Array-stacked operation
'''
import sys

# declaring empty stack
queue = []
op = 0 # For storing options and adding number
print("\n-------Queue in Python-------\n")

# Stack operation begins here
while(True):
    print("Please enter the options:")
    print("1. Enqueue  2. Dequeue  3. Display  4. Exit")
    op = int(input())
    if(op == 1):
        op = int(input("\nEnter the number to be appended: "))
        queue.append(op)
    elif(op == 2):
        print('\nElements poped from stack:') 
        print(queue.pop(0)) 
    elif(op == 3):
        print(queue)
    elif(op == 4):
        print("\nExiting...")
        break
    else:
        print("\nWrong input...Try again\n")
    
