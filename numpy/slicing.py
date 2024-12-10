import numpy as np

aar = np.arange(10)
print(aar, type(aar))
print(aar[1:5]) #slicing


#Slicing 2-D array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2[:, 1:3])