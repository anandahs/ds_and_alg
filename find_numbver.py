import numpy as np

array1 = np.array([1, 23, 6, 7, 8, 10, 11, 121, 31, 112, 31, 1])
num = 8
for i in range(len(array1)):
    if array1[i] == num:
        print(f"{num} is found at {i}")
