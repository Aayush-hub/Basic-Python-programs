#python program to check given given number is niven number or not
n=int(input("Enter an integer number:"))
sum=0
temp=n
while n!=0:
    r1=n%10
    sum=sum+r1
    n=n//10
    r2=temp%sum
if r2==0:
    print(temp,"is a niven number.")
else:
    print(temp,"is not niven number.")
