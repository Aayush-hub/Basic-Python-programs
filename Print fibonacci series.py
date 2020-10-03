n=int(input("Enter the number of terms "))
a,b = 0, 1
count=0

# check if the number of terms is valid
if n<= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence :")
   print(a)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(a)
       c=a + b
       a = b
       b = c
       count += 1
