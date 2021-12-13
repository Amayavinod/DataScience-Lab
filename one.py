#NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.


import numpy as np
x = np.array([3, 5,10,56])
y = np.array([2, 5,6,78])
print("Original numbers:")
print(x)
print(y)
print("Comparison - greater")
print(np.greater(x, y))
print("Comparison - greater_equal")
print(np.greater_equal(x, y))
print("Comparison - less")
print(np.less(x, y))
print("Comparison - less_equal")

print(np.less_equal(x, y))
