# 1-Array will zeroes only
import numpy as np
a = np.zeros(3,dtype=int)
for x in a:
    print(x)

#Multi-Dimensional Array Creation
b = np.zeros((1,1))
print(b)

#Same for ones(1-d and multi follows same as zeros)
b = np.ones((1,1))
print(b)

b=np.random.rand(1,5)
print(b)

#Filling array with custom value
c = np.full(2,"Khushii")
print(c)

#Arrange creating array in some sequnce
#(start,end,gap)
d = np.arange(1,10,2)
print(d)

#Loop way
for x in range(1,10,2):
    print(x)
    