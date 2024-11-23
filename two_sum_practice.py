def two_sum_problem(data_list, two_sum):
    seen = dict()
    data_length = len(data_list)

    if data_length == 0:
        return -1, -1

    else:

        for i in range(data_length):
            compliment = two_sum - data_list[i]

            if compliment in seen:
                return seen[compliment], i
            else:
                seen[data_list[i]] = i


def max_problem(data_list, max_type="sum"):
    max_num1 = 0
    max_num2 = 0

    for num in data_list:
        if num > max_num1:
            max_num2 = max_num1
            max_num1 = num
        elif num > max_num2:
            max_num2 = num

    if max_type == "product":
        return max_num1 * max_num2
    else:
        return max_num1 + max_num2


if __name__ == "__main__":
    data_list = [9, 8, 7, 10, 13]
    two_sum = 23
    print(two_sum_problem(data_list, two_sum))
    print(f"max product:{max_problem(data_list, 'product')}")
    print(f"max sum:{max_problem(data_list, 'sum')}")
