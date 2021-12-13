
#NumPy program to check whether two arrays are equal (element wise) or not

import numpy as np
nums1 = np.array([0.5, 1.5, 0.2])
nums2 = np.array([0.4999999999, 1.500000000, 0.2])
np.set_printoptions(precision=15)
print("Original arrays:")
print(nums1)
print(nums2)
print("\nTest said two arrays are equal (element wise) or not:?")
print(nums1 == nums2)
nums1 = np.array([0.5, 1.5, 0.23])
nums2 = np.array([0.4999999999, 1.5000000001, 0.23])
print("\nOriginal arrays:")
np.set_printoptions(precision=15)
print(nums1)
print(nums2)
print("\nTest said two arrays are equal (element wise) or not:?")
print(np.equal(nums1, nums2))
