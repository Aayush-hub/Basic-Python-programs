import sys

#Declaring satic list
#Can be changed to dynamic in futher modification easily
A = [64, 25, 12, 22, 11]

#Tansversing through the list
for i in range(len(A)):
    #Here we need to find the smallest element in the dynamic defined range
    minimum_index = i
    for j in range(i+1, len(A)):
        if A[minimum_index] >A[j]:
            minimum_index = j

    #Swapping the elements
    A[i], A[minimum_index] = A[minimum_index], A[i]

print("Initial array is: ")
print(A)
print("The sorted array is: ")
print(A)