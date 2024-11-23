import numpy


# time complexity O(n)
# space complexity O(n) to hold seen values, this in worst case
def two_sum(items, target):
    seen = {}

    for index, value in enumerate(items):
        compliment = target - value

        if compliment in seen:
            return seen[compliment], index
        seen[value] = index

    return -1, -1


# time complexity O(n^2)
# space complexity is O(n) to store the results:
def pair_sum(arr, target_sum):
    pairs = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append(f"{arr[i]}+{arr[j]}")

    return pairs


if __name__ == "__main__":
    items = [100, 200, 300, 400, 500, 600]
    target = 700
    print(two_sum(items, target))
    arr = numpy.array([2, 4, 3, 5, 6, -2, 4, 7, 8, 9])
    target_sum = 7
    print(pair_sum(arr, target_sum))
