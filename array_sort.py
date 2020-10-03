#Taking user input to create an array of elements
arr = []
n = int(input("Enter the number of elements: "))
for i in range(0, n):
    ele = int(input("Enter number: "))
    arr.append(ele)

#Ascending order function
def asc(arr):
    for i in range(0, len(arr)):    
        for j in range(i+1, len(arr)):    
            if(arr[i] > arr[j]):    
                temp = arr[i];    
                arr[i] = arr[j];    
                arr[j] = temp;    

#Descending order function
def desc(arr):
    for i in range(0, len(arr)):    
        for j in range(i+1, len(arr)):    
            if(arr[i] < arr[j]):    
                temp = arr[i];    
                arr[i] = arr[j];    
                arr[j] = temp; 

#Taking user input for sorting the array
sort = input("How do you want to sort the array? Type *asc* for ascending order or *desc* for descending order: ")

#Performing the sort based on the user's input
if(sort == "asc"):
    print("Ascending order: ")
    asc(arr)
    for i in range(0, len(arr)):     
        print(arr[i], end=" ")
else:
    print("Descending order: ")
    desc(arr)
    for i in range(0, len(arr)):     
        print(arr[i], end=" ")
