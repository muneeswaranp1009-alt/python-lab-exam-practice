#8. Write a program to demonstrate functions in Python Libraries using NumPy

import numpy as np

arr = np.array([4,5,2,3,6,1])

print('\nArray :',arr)

print('\nArray Shape :',arr.shape)
print('Array Datatype :',arr.dtype)

print('\nArray Sum :',arr.sum())
print('Array Mean :',np.mean(arr))
print('Array Minimum :',np.min(arr))
print('Array Maximum :',arr.max())
print('Array Square Root :',np.sqrt(arr))

matrix = np.arange(6).reshape(2,3)
print('\nReshaped Array :',matrix)

a = np.array([1,2,3])
b = np.array([4,5,6])

print('\nAddition :',a + b)
print('Multiplication :',a*b)

print("\nSorted Array :",np.sort(arr))

print('\nRandom Array :',np.random.randint(1,10,3))