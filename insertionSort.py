# Function to do insertion sort 
def InsertionSort(A): 
  
    #For Transversing
    for i in range(1, len(A)): 
  
        key = A[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < A[j] : 
                A[j+1] = A[j] 
                j -= 1
        A[j+1] = key 
  
  
#Defining static list but code can modified for making it dynamic list 
A = [21, 65, 95, 82]
print("initial Array is: ")
print(A)
InsertionSort(A) 
print("Sorted array is:") 
print(A)