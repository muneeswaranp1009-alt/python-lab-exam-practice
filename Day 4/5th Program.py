#5. Write a python program using fancy indexing

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print('\nOrginal Array:',arr)
indices = [0,2,4,1,5]
print("\nSelected Indices:",arr)

fancy_indices = arr[indices]
print("\nElements using fancy indices:",fancy_indices)