# A deep copy breaks all references to the original and creates a new object.
# This means that changes made to the nested objects in the original or copied object
# will not affect each other. See the example below:

# Now that we have created a deep copy, the changes that we have made to the deep copy have no effect on the original list.
# So, knowing the difference between shallow copy
# and deep copy will ensure that you choose the appropriate method based on your specific requirements.

import copy

list_of_numbers = [[1, 2, 3], [4, 5, 6]]

shallow_copy_list = copy.deepcopy(list_of_numbers)

shallow_copy_list[0][0] = 0

print(f"original list:{list_of_numbers}")
print(f"deep copy:{shallow_copy_list}")

dictionary_example = {"A": [1, 2, 3], "B": [4, 5, 6]}

dictionary_example_shallow_copy = copy.deepcopy(dictionary_example)

dictionary_example_shallow_copy["A"] = [0, 2, 3]

print(f"original dictionary:{dictionary_example}")
print(f"deep copy dictionary:{dictionary_example_shallow_copy}")
