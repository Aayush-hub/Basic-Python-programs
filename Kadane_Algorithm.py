'''
Kadane's Algorithm:
The maximum sum subarray problem is the task of finding a contiguous subarray with the largest sum, within a given one-dimensional array A[1...n] of numbers.
This is one of the most popular problems and is asked in almost all of the Technical Interviews of top Companies.
Kadne's algorithm can be used to find the sum of the largest sum contiguous subarray or modified to find the subarray itself.

Contributor's Note:
This is a pretty easy algorithm to understand, although, seems a little scary by its name. I faced this problem in the interviews of companies like Walmart and Amazon.

For a Video based Explanation, check out my favorite video on this topic:
https://youtu.be/jnoVtCKECmQ

'''

def kadane(arr):
    max_val = arr[0]
    current = max_val

    for x in range(1,len(arr)):
        current = max(arr[x]+current,arr[x])
        max_val = max(current,max_val)

    return max_val


inp_list = list(map(int,input().split()))
print("Maximum contiguous subarray sum is : "+str(kadane(inp_list)))
