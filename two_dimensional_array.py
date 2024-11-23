import numpy as np

two_dimensional_array = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

row_two_dimensional_array = np.insert(two_dimensional_array, 0, [[1, 2, 3, 4]], axis=0)

column_two_dimensional_array = np.insert(two_dimensional_array, 0, [[1, 2, 3, 4]], axis=1)

column1_two_dimensional_array = np.insert(two_dimensional_array, 1, [[1, 2, 3, 4]], axis=1)

print(row_two_dimensional_array)
print(column_two_dimensional_array)
print(column1_two_dimensional_array)

append_two_row_dimensional_array = np.append(two_dimensional_array, [[1, 2, 3, 4]], axis=0)

print(two_dimensional_array)

# append_two_column_dimensional_array = np.append(two_dimensional_array, [[1, 2, 3, 4]], axis=1)
# print(append_two_row_dimensional_array)
# print(append_two_column_dimensional_array)
