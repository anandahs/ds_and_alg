# 2. Avoid Unintended Side Effects with Default Arguments
# Another common pitfall in Python involves mutable default arguments in function definitions.
# In the example below, we have defined a function with a default argument, which is an empty list.
# This leads to unpredictable behavior.

def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list


# call function first time.
result1 = append_to_list(1)

print(f"result1:{result1}")

# call function second time.
result2 = append_to_list(2)

print(f"result2:{result2}")

# call function first time.
result3 = append_to_list(3)

print(f"result3:{result3}")


# Have you noticed what is happening here? Each subsequent call to the function without explicitly providing a my_list argument will reuse this same list object,
# leading to unexpected results.
# In this code, when we call the function for the first time without providing an argument for the my_list variable,
# the function appends 1 to my_list, and it returns my_list. The result1 variable now contains [1].
#
# When we call the function the second time, it appends 2 to the same list (now [1, 2]) and returns it.
# When we call the function the third time, it appends 3 to the same list (now [1, 2, 3]) and returns it.
# So, each subsequent call to append_to_list modifies the same default list,
# which accumulates elements from previous calls This is unexpected behavior
# if you assume that each call to the append_to_list function starts with an empty list.
#
# The reason for this behavior is that the default value for the my_list variable is created only once,
# at the time the function is defined. This default list is then used and modified every time the function is called without
# explicitly passing a value for my_list.
#
# To avoid this unexpected behavior, you can pass an immutable object as a default argument.
# For example, you can pass "None" as the default argument and only initialize the empty list inside the function when the default argument is None.
# This will ensure that each call to the function works with a distinct list, preventing the issue of shared references. See the modified code below:

def append_to_list_modified(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


# call function first time.
result1 = append_to_list_modified(1)

print(f"result1:{result1}")

# call function second time.
result2 = append_to_list_modified(2)

print(f"result2:{result2}")

# call function first time.
result3 = append_to_list_modified(3)

print(f"result3:{result3}")

my_number = 5
another_number = 10

if my_number is another_number:
    print("numbers are equal")
else:
    print("numbers are not equal")

my_list = [5]

my_another_list = [5]

if my_list is my_another_list:
    print("lists are equal")
else:
    print("lists are not equal")

# Here, we are getting "The lists are not equal," even though the lists have the same values.
# This is inconsistent with the results in the previous example.
# You would have expected the lists to be equal, too.
# The unexpected results are because of the behavior of the "is" operator.
# The "is" operator is not comparing if the two values are equal. The "is" operator checks for object identity.
# It determines whether both operands refer to the exact same object in memory. In the first example,
# we get "The numbers are equal" because the two integers are the same object in memory.
# This is because in Python, if you create two immutable objects with the same value,
# they might actually point to the same object in memory. In the second example,
# we get "The lists are not equal,
# " because the two lists (mutable objects) are not the same object in memory even though they have the same elements.
# To avoid this behavior, use the equality operator (==) to check if objects are equal.

my_list = [5]

my_another_list = [5]

if my_list == my_another_list:
    print("lists are equal")
else:
    print("lists are not equal")

#tuple is immutable, lets see what happens

my_tuple = (5,10)

my_another_tuple = (5,10)

if my_tuple is my_another_tuple:
    print("tuples are equal")
    # This is because in Python,
    # if you create two immutable objects with the same value, they might actually point to the same object in memory.
else:
    print("tuples are not equal")