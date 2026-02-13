import numpy as np

nums = list(map(int, input("Enter the list of integers (space-separated): ").split()))

arr = np.array(nums, dtype=float)

print(arr)