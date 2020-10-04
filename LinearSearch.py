def LinearSearch(num, key):
    for i in range(len(num)):
        if num[i] == key:
            return i
    return -1


num_list = input('Enter the list of numbers: ')
num_list = num_list.split()
num_list = [int(x) for x in num_list]
key = int(input("Enter Item to search: "))
index = LinearSearch(num_list, key)
if index < 0:
    print(f'{key} is not on the list')
else:
    print(f'{key} is on the {index} index on th list')

