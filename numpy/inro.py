import numpy as np

#numpy ---> numeric python 
#ndarrays --> n-dimensional arrays

arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr.shape)

#range
arrSecond = np.arange(0,10,3)
print(arrSecond)

#Muiltidimentional Zeros

arr3 = np.zeros((3,10))
print(arr3)
print(arr3.shape)

#Full
aar4 = np.full((10),77)
print(aar4)

#Multidimentional Full
aar5  = np.full((2,10), 7700)
print(aar5)

#Accessing 
print(aar5[0][1])