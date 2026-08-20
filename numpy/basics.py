#In this section we will learn about the basic of numpy

#Importing numpy
import numpy as np

#Basic array creation
array = np.array([1,2,3,"adarsh"])

print(array)
#This will give the number of row and col

print(array.shape)

#This will give total size
print(array.size)

b = np.array([[1,3,4],[2,3,4]] , dtype=object)
print(b.shape)
print(b.size)

#Loop on numpy array

for i in b:
    for j in i:
        print(j)


#ndim tells you how many dimensions (axes) an array has.
print(b.ndim)