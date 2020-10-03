arr=[]
len=int(input("Enter the size of array"))

for i in range(len):
    a=int(input("Enter the array"))
    arr.append(a)

print(arr)

x=int(input("Enter the element to be searched for"))

beg=0
end=len-1
mid=(beg+end)//2
flag=0

while(beg<=end):
    if(arr[mid]==x):
        print("Element found at position : %s" % (mid+1))
        flag=1
        #break

    if(arr[mid>x]):
        end=mid-1
        mid = (beg + end) // 2

    else:
        beg=mid+1
        mid = (beg + end) // 2

if(flag==0):
    print("Element not found")


