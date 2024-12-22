def shift_zeroes_to_end(nums):
    left = 0

    for right in range(len(nums)):

        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1

    return nums


if __name__ == "__main__":
    print(shift_zeroes_to_end([0, 1, 0, 3, 2]))
    print(shift_zeroes_to_end([0, 1, 0, 3, 0, 0, 0, 2]))
