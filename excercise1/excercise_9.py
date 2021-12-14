
#NumPy program to create a 4x4 array with random values, now create a new array from the said array swapping first and last rows.

import numpy as np 
nums = np.arange(16, dtype='int').reshape(-1, 4)
print("Original array:")
print(nums)
print("\nNew array after swapping first and last rows of the said array:")
new_nums = nums[[3,1,2,0]]
print(new_nums)
