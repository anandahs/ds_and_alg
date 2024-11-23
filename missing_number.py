def missing_number(items, n):
    total = (n * (n + 1)) / 2
    sum_of_items = sum(items)
    missing_num = total - sum_of_items
    return int(missing_num)


if __name__ == "__main__":
    data = [1, 2, 4, 5, 6, 7, 8]
    print(f"missing_number:{missing_number(data, 8)}")
