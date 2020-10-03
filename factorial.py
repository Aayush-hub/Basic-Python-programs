'''
python program to get a factorial of number
''' 
def factorial(n): 
      
    # recursive function to get a factorial of number
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
  
# Driver Code 
num = int(input())
print("Factorial of",num,"is", 
factorial(num)) 