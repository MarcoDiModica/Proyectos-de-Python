#NumPy

import numpy as np

arr = np.array([x for x in range(6)]) #array created with numpy, we also can create tuples and more #1D array
arr1 = np.array(np.random.randint(1,100)) #0D array
arr2 = np.array([[x for x in range(6)], [x for x in range(6)]])

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print(arr1)
print(0.2+0.1)
#print(np.__version__)
#print(type(arr))