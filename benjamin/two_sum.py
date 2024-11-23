class Solution:

    @staticmethod
    def two_sum(nums, target):
        '''
        :param nums: list of integers
        :param target: sum of two indices in list
        :return: indices of two indices of numbers that sum upto to target
        '''
        
        h = {}

        for i, n in enumerate(nums):
            h[n] = i

        for i, num in enumerate(nums):
            desired = target - num

            if desired in h and h[desired] != i:
                return i, h[desired]


nums = [7, 5, 9, 4]
answer = Solution.two_sum(nums, 9)
print(f"{answer}")
