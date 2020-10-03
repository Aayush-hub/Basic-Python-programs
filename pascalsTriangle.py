#Python Program to implement pascals triangle
def PrintPascal(n:int):
    pascal = [[0 for x in range(n)]
                  for y in range(n)]   #dummy array to store the values of pascal triangle
    
    #printing every line of it
    for line in range(0,n):
        #Number of intergers is equal to line number
        for i in range(0, line+1):

            if(i == 0 or i == line):
                pascal[line][i] = 1
                print(pascal[line][i], end =" ")   #As first and last value in every row is one
            
            else:
                pascal[line][i] = (pascal[line - 1][i-1]+pascal[line - 1][i])
                print(pascal[line][i], end = " ")

        print("\n", end = "")

n = int(input("Enter the value of pascal triangle rows: "))
PrintPascal(n)