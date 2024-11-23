# Time complexity:
#
# The overall time complexity of this function is O(n), where n is the number of elements in the dictionary my_dict. This is determined by the dictionary comprehension, which iterates through all the key-value pairs in the input dictionary.
#
# Space complexity:
#
# The space complexity of this function depends on the number of elements in the filtered dictionary, which in turn depends on the condition function. In the worst case, when all key-value pairs meet the condition, the space complexity is O(n), where n is the number of elements in the dictionary my_dict. In the best case, when no key-value pairs meet the condition, the space complexity is O(1) as the function creates an empty dictionary.

def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}



if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
    print(filtered_dict)
