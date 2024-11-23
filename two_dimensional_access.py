import numpy as np

two_dimensional_array = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])


# print(len(two_dimensional_array))
#
# print(two_dimensional_array[0])


def access_elements(array, row_index, column_index):
    if row_index >= len(two_dimensional_array) or column_index >= len(two_dimensional_array[0]):
        raise Exception('incorrect index')
    return array[row_index][column_index]


if __name__ == "__main__":
    print(access_elements(two_dimensional_array, 5, 2))
