from collections import Counter

# Define an inner function count_elements(lst) that counts the frequency of elements in a list lst. The function creates an empty dictionary counter, iterates through the list, and increments the count for each element using the get() method. The get() method takes O(1) average time complexity. The function returns the counter dictionary. The time complexity of count_elements() is O(n), where n is the number of elements in the input list lst. The space complexity is also O(n), as the dictionary counter has as many keys as there are distinct elements in the list.
#
# Call the count_elements() function on both input lists list1 and list2. This operation has a time complexity of O(n1 + n2), where n1 and n2 are the lengths of list1 and list2, respectively. The space complexity is O(m1 + m2), where m1 and m2 are the numbers of distinct elements in list1 and list2, respectively.
#
# Compare the resulting dictionaries using the == operator. This operation has a time complexity of O(min(m1, m2)), as it compares the keys and values of both dictionaries.
# 
# Return the result of the comparison (True if the dictionaries are equal, False otherwise).
#
# Time complexity:
#
# The overall time complexity of this function is O(n1 + n2 + min(m1, m2)), where n1 and n2 are the lengths of list1 and list2, and m1 and m2 are the numbers of distinct elements in list1 and list2, respectively. This is determined by the time complexity of the count_elements() function and the dictionary comparison.
#
# Space complexity:
#
# The space complexity of this function is O(m1 + m2), where m1 and m2 are the numbers of distinct elements in list1 and list2, respectively. This is because the function creates two dictionaries with as many keys as there are distinct elements in the input lists.


def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter

    return count_elements(list1) == count_elements(list2)


def check_same_frequency(list1, list2):
    list1_counter = Counter(list1)
    list2_counter = Counter(list2)

    print(list1_counter)
    print(list2_counter)

    # if len(list1_counter) != len(list2_counter):
    #     return  False
    # else:
    #     for key, value in list1_counter.items():
    #         if list2_counter.get(key,0) != value:
    #             return False
    # return True

    return list1_counter == list2_counter


list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))

list3 = [1, 2, 3, 2, 1]
list4 = [1, 2, 2, 3, 1]

print(check_same_frequency(list3, list4))
