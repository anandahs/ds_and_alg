# input list = [1, 1, 1, 2, 2, 0, 0, 5, 5, 10, 10]
# occurance k = 2
# expected output = [ 2,0,5,10]
import sys
from collections import Counter


def get_k_list(input_list, k):
    counter_dict = Counter(input_list)

    k_list = []
    for number, count in counter_dict.items():
        if count == k:
            k_list.append(number)

    return k_list


def two_sum():
    input_list = [1, 2, 4, 5, 6, 10]
    sum = 16

    lookup = {}
    for index, value in enumerate(input_list):
        lookup[value] = index

    for i, num in enumerate(input_list):
        desired = sum - num
        if desired in lookup and i != lookup[desired]:
            return i, lookup[desired]


if __name__ == '__main__':
    # print(len(sys.argv))
    # if len(sys.argv) != 3:
    #     print("Usage: K_elements <input_list> <k>")
    #
    # else:
    #     in_list = sys.argv[1]
    #     k = sys.argv[2]
    in_list = [1, 1, 1, 2, 2, 0, 0, 5, 5, 10, 10]
    k = 2
    print(get_k_list(input_list=in_list, k=k))
    print(f"two numbers are found at indices : {two_sum()}")
