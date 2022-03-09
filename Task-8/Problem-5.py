# Addition of Arrays    
import numpy as np

in_arr1 = np.array([2, -7, 5])
in_arr2 = np.array([5, 8, -5])

print ("1st Input array : ", in_arr1)
print ("2nd Input array : ", in_arr2)
	
add = np.add(in_arr1, in_arr2)
print ("output added array :\n ", add,"\n")

# Multiplication of Arrays
# 2D
m1 = np.array([[1, 3, 4], [1, 5, 5]])
m2 = np.array([[1, 4], [2, 5], [3, 6]])
print("\n m1:", m1, "\n m2:", m2)
m3 = np.dot(m1, m2)
print("\nm1*m2 =", m3)

#3D
m1 = ([1, 4, 5], [1, 6, 9], [2, 11, 31])
m2 = ([0, 6, 5], [5, 6, 7], [9, 5, 12])
print("\n m1:", m1, "\n\nm2:", m2,"\n")
m3 = np.dot(m1, m2)
print("m1*m2 =", m3)
