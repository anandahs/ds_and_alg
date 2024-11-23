import numpy as np

two_dimensional_array = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

# time complexity O(mn)
# space complexity O(1)

def search_2d_array(array, value):
    for i in range(len(array)):  # O(m*n)
        for j in range(len(array[0])):  # O(n)
            if value == array[i][j]: #O(1)
                return f'the {value} is located at index {i}{j}'
    return 'The {value} is not found'


print(f'two dimentional array{two_dimensional_array}')
print(search_2d_array(two_dimensional_array, 14))
print(search_2d_array(two_dimensional_array, 55))
