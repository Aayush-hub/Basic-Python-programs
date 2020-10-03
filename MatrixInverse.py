'''
Python program is to get a inverse of a matrix using 
''' 
  
# Import required package 
import numpy as np 
  
# Taking a 3 * 3 matrix 
A = np.array([[6, 1, 1], 
              [4, -2, 5], 
              [2, 8, 7]]) 
  
# Calculating the inverse of the matrix 
print(np.linalg.inv(A))