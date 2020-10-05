arr = [int(i) for i in input('Enter Elements\n').split()]

mx = max(arr)
mn = min(arr)

count = [0 for i in range(mx+1+abs(mn))] # Adding minimum element to make all the indexing postive.

for i in arr:
  count[i+mn]+=1

arr=[]

for i in range(len(count)):
  while count[i] > 0:
    count[i]-=1
    arr.append(i-mn)

print('Sorted Array :')

print(arr)
