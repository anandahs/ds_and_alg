def triple_sum_brute_force(nums):
    """
    :param nums:
    :return list of triples:
    """
    n = len(nums)

    triplets = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):

                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    triplets.add(triplet)

    return [list(triplet) for triplet in triplets]


def two_pairs_sum_sorted(nums_input, start_index, target):
    left, right = start_index, len(nums_input) - 1

    pairs = []

    while left < right:

        sum_of_two = nums_input[left] + nums_input[right]

        if sum_of_two == target:
            pairs.append([nums_input[left], nums_input[right]])
            left += 1

            while left < right:
                if nums_input[left] == nums_input[right - 1]:
                    continue
        elif sum_of_two < target:
            left += 1
        else:
            right -= 1

    return pairs


# Time complexity
#  O(nlogn) -  sorting
#  O(n2) - traversal, since for each element, rest of the elements are checked.
#  overall time complexity is O(nlogn) + O(n2) = O(n2)
#  space complexity
#  O(n) for sorting
#  O(n2) for adding triplets,
#  O(n2) because  two_pairs_sum_sorted, can add n pairs to the output at worst case
#  and also, it would be called approximately n times
#  so, space complexity would be O(n) + O(n2) = O(n2)
def triple_sum_efficient(nums_input):
    triplets = []
    nums_input.sort()

    for i in range(len(nums_input)):

        if nums_input[i] > 0:
            break
        if i > 0 and nums_input[i] == nums_input[i - 1]:
            continue

        pairs = two_pairs_sum_sorted(nums_input, i + 1, -nums_input[i])

        for pair in pairs:
            triplets.append([nums_input[i]] + pair)

    return triplets


if __name__ == "__main__":
    nums = [0, -1, 2, -3, 1]

    print(triple_sum_brute_force(nums))
    print(triple_sum_efficient(nums))
