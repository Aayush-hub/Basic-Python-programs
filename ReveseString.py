#Program to reverse a list

# Function to reverse list from starting to end
def reverseList(string, start, end):
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1 

# main function
if __name__ == "__main__":
    A = [1, 2, 3, 4,]
    print(A)
    reverseList(A, 0, 3)
    print("The Reversed list is :")
    print(A)
