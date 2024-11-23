import numpy as np

two_dimensional_array = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

for i in range(len(two_dimensional_array)):  # O(m*n)
    for j in range(len(two_dimensional_array[0])):  # O(n)
        print(two_dimensional_array[i][j])  # O(1)

