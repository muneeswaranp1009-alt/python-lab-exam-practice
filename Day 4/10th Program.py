# 10. Write a program to demonstrate functions in Python Library using Scikit

import numpy as np
import matplotlib.pyplot as plt 
from sklearn.datasets import make_blobs

x,_ = make_blobs(n_samples= 500,centers=4,random_state= 0)
y = np.logical_xor(x[:,0]>0 , x[:,1]>0)

plt.scatter(x[:,0] , x[:,1] , c=y)

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title("XOR TAble using Scikit")
plt.show()