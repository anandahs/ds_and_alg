def two_pairs_sorted(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        sum_of_two = nums[left] + nums[right]

        if sum_of_two < target:
            left += 1
        elif sum_of_two > target:
            right -= 1
        else:
            return [left, right]

    return []


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    # target = 6
    print(two_pairs_sorted(nums, 13))
    print(two_pairs_sorted(nums, 9))
    print(two_pairs_sorted(nums, 98))
    print(two_pairs_sorted(nums, 1))
    print(two_pairs_sorted(nums, 9))
    print(two_pairs_sorted(nums, 7))
