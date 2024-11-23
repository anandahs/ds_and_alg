import array
import numpy as np

my_array0 = array.array('i', [])  # time and space complexity is O(1),
# it creates array with just metadata and no elements

print(f"my_array0:{my_array0}")

my_array1 = array.array('i', [1, 2, 3, 4])  # time and space complexity is O(n) -  as number of elements increases,
# the space and time complexity increase as it needs more memory and time(number of operations)

print(f"my_array1:{my_array1}")

my_array1.insert(0, 6)

print(f"my_array1 after insertion:{my_array1}")

my_array1.insert(100, 6)  # this inserts at the end no matter how far index is given here

print(f"my_array1 after inserting at 100th position:{my_array1}")

my_numpy_array0 = np.array([], dtype=int)  # time and space complexity is O(1)

print(f"my_numpy_array:{my_numpy_array0}")

my_numpy_array1 = np.array([1, 2, 3, 4], int)  # time and space complexity is O(n)

print(f"my_numpy_array1:{my_numpy_array1}")

# searching an element from array

arr1 = array.array('i', [1, 2, 3, 4, 5, 6])


def access_element(array_data, index):
    if index < 0 or index >= len(array_data):  # ----O(1)
        print("there is not element in this index")
    else:
        data_element = array_data[index]  # ----O(1)
        print(f"element at index:{index} is {data_element}")  # ----O(1)


# so space and time-complexity is O(1) -  constant
access_element(arr1, -1)
access_element(arr1, 2)
access_element(arr1, 100)
access_element(arr1, 6)


def linear_search(array_data, target):
    for i in range(len(array_data)):  # O(n)
        if array_data[i] == target:  # O(1)
            return i  # O(1)
    return -1  # O(1)


element = 6
# element = 20
element_index = linear_search(arr1, element)
if element_index == -1:
    print(f"element:{element} is not available in array:{arr1}")
else:
    print(f"element:{element} is available at index:{element_index} in array:{arr1}")

array_data1 = array.array("i", [1, 2, 3, 4, 5, 6])

array_data1.remove(6)  # O(n) for worst case if element is deleted from first index,
# O(1) if element is deleted at the end since data movement is not required
# space complexity is O(1) since extra space is not required for delete operation
print(array_data1)
