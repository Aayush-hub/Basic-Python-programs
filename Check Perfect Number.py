n=int(input('Enter the number:'))
i=1
sum=0
while i<n:
	if n%i==0:
		sum=sum+i
	i+=1
if n==sum:
	print("It is a perfect number")
else:
	print("It is not a perfect number")	

