def get_odd_list1(input_list):
    odd_list_1 = []
    for data in input_list:
        if data % 2 == 0:
            continue
        else:
            odd_list_1.append(data)
    return odd_list_1


def get_odd_list2(input_list):
    odd_list_2 = [data for data in input_list if data % 2 != 0]
    return odd_list_2


def get_flatten_list(input_list):
    flat_list = []

    for nested_input_list in input_list:
        for data in nested_input_list:
            if data not in flat_list:
                flat_list.append(data)
    return flat_list


def get_flatten_list_iters(input_list):
    from itertools import chain
    return list(set(chain.from_iterable(input_list)))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    odd_list1 = get_odd_list1(my_list)
    print(f"odd_list1:{odd_list1}")
    odd_list2 = get_odd_list2(my_list)
    print(f"odd_list2:{odd_list2}")

    nested_list = [[1, 2, 3], [2, 3, 6]]
    flatten_list = get_flatten_list(nested_list)
    print(f"flatten_list:{flatten_list}")
    flatten_list_iters = get_flatten_list_iters(nested_list)
    print(f"flatten_list_iters:{flatten_list_iters}")
