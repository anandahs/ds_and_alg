def two_sums(data_items, target):
    dict = {num: i for i, num in enumerate(data_items)}
    # print(dict)

    for item in data_items:
        desired = target - item

        if desired in dict.keys():
            index1 = dict[item]
            index2 = dict[desired]

            if index1 == index2 + 1:
                return index2, index1
                break


def two_sums_instructor(data_items, target):
    seen = {}
    for key, value in enumerate(data_items):

        complement = target - value

        if complement in seen:
            return seen[complement], key
        else:
            seen[value] = key


if __name__ == "__main__":
    target = 30
    data_items = [2, 4, 3, 1, 10, 20, 50]
    print(two_sums(data_items, target))
    print(two_sums_instructor(data_items, target))
