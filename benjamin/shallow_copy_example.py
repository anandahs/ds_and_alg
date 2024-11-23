# 1. Stop Making Shallow Copies of Mutable Objects
# Creating copies of objects is a very common practice when writing Python code.
# Usually, copies are made because you want to ensure that changes in the copy don't affect the original, and vice versa. However,
# this is not the case when you make a shallow copy of data structures like lists or dictionaries that contain mutable objects (lists, dictionaries, etc.)
# within them. Let's see the following example:


# In this code, you can see that changes made to the shallow_copy's nested list are also reflected in the original list.
# So, if your intention is to create a copy of a list so that changes made to the copy do not affect the original,
# then do not create a shallow copy. This unpredictable behavior is because the shallow copy only creates a new reference for
# the top-level object, but nested mutable objects are still referenced by both the original and the copy.

import copy

list_of_numbers = [[1, 2, 3], [4, 5, 6]]

shallow_copy_list = copy.copy(list_of_numbers)

shallow_copy_list[0][0] = 0

print(f"original list:{list_of_numbers}")
print(f"Shallow copy:{shallow_copy_list}")

dictionary_example = {"A": [1, 2, 3], "B": [4, 5, 6]}

dictionary_example_shallow_copy = copy.copy(dictionary_example)

dictionary_example_shallow_copy["A"] = [0, 2, 3]

print(f"original dictionary:{dictionary_example}")
print(f"Shallow copy dictionary:{dictionary_example_shallow_copy}")

x = [[1, 2, 3], [4, 5, 6]]
y = x.copy()
y += [10,20,30]
print(x)
print(y)
