import numpy as np

# time complexity of delete O(mn)
# space complexity of delete O(mn), it has to move all the elements.

two_dimensional_array = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

print(f'original array:\n{two_dimensional_array}')

d_dimensional_column_array = np.delete(two_dimensional_array, 0, axis=1)
print('0th column deleted ')
print(d_dimensional_column_array)

print('1st row deleted ')
d_dimensional_row_array = np.delete(two_dimensional_array, 1, axis=0)
print(d_dimensional_row_array)
