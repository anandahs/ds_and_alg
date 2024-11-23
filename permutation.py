def permutation(list1, list2):
    if len(list1) != len(list2):
        return False

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True

    return False


def permutation2(list1, list2):
    if len(list1) != len(list2):
        return False

    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    if sorted_list1 == sorted_list2:
        return True

    return False


if __name__ == "__main__":
    list1 = [1, 2, 3, 4]
    list2 = [4, 3, 2, 1]
    list3 = [1, 2, 10, 4]
    list4 = [4, 3, 2, 1]
    print(permutation(list1, list2))
    print(permutation2(list1, list2))
    print(permutation2(list3, list4))
