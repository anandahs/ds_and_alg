from functools import reduce

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

results1 = list(zip(my_strings, my_numbers))

print(results)
print(results1)

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: x, my_floats))
filter_result = list(map(lambda name: name[::-1], my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 1)

print(f"map_result:{map_result}")
print(f"filter_result:{filter_result}")
print(f"reduce_result:{reduce_result}")


def custom_sum(num1, num2):
    if len(num1) != len(num2):
        raise ValueError("Input tuples must have the same length.")

    sum1, sum2 = 0, 0

    if type(num1) is not tuple:
        sum1 = num1
    else:
        for i in num1:
            sum1 += i

    if type(num2) is not tuple:
        sum2 = num2
    else:
        for j in num2:
            sum2 += j
    return sum1 + sum2


def tuple_elementwise_sum(tuple1, tuple2):
    total_sum = reduce(custom_sum, zip(tuple1, tuple2))
    return total_sum, tuple(map(sum, zip(tuple1, tuple2)))


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(f"tuple1:{tuple1}")
print(f"tuple2:{tuple2}")
print(type(tuple1) is tuple)


# print(tuple_elementwise_sum(tuple1, tuple2))


def sum_product(input_tuple):
    sum_result = 0
    product_result = 1

    for i in input_tuple:
        sum_result += i
        product_result *= i

    return sum_result, product_result


print(sum_product((1, 2, 3, 4)))


#
# new_tuple = ('a', 'b', 'c', 'd', 'e')
#
# print(type(new_tuple))
#
# new_tuple = ('abcde',)
# print(type(new_tuple))
#
# new_tuple = 'a', 'b', 'c', 'd', 'e', 'a'
# new_tuple1 = 'a', 'b', 'c', 'd', 'e', 'a'
# print(type(new_tuple))
#
# for i in new_tuple:
#     print(i)
#
# for i in range(len(new_tuple)):
#     print(new_tuple[i])
#
# print(new_tuple.index('a'))
# print(new_tuple.count('a'))
#
# print(new_tuple + new_tuple1)
# print(new_tuple * 4)

def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))


input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(f"diagonal:{get_diagonal(input_tuple)}")


def insert_value_front(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple


input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)  # E


# return tuple(set(tuple1) & set(tuple2)) - This line creates two sets from the input tuples using the set() constructor,
# and then computes the set intersection using the & operator.
# The time complexity of creating each set is O(n), where n is the length of the input tuple.
# The time complexity of computing the set intersection is O(min(n,m)), where m is the length of the second input tuple.
# Since the two input tuples are of equal length, the overall time complexity of the function is O(n).
# The space complexity is also O(n) because the size of the resulting set will be no larger than the size of the smaller of the two input tuples.
def common_set_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))


def common_elements(tuple1, tuple2):


    return tuple(item for item in tuple1 if item in tuple2)


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
output_tuple = common_set_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)
