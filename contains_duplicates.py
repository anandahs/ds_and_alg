def contain_duplicates(arr):
    seen = set()

    for item in arr:
        if item in seen:
            return True
        else:
            seen.add(item)

    return False


if __name__ == "__main__":
    arr = [1, 2, 2, 2, 5, 1, 2, 1, 2]
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(contain_duplicates(arr))
    print(contain_duplicates(arr1))
