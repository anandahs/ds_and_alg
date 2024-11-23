def product_except_self(nums):
    product_length = len(nums)
    if product_length == 0:
        return []
    else:
        results = [1] * product_length
        left_product = 1

        for i in range(product_length):
            results[i] = left_product
            left_product *= nums[i]

        right_product = 1

        for i in range(product_length - 1, -1, -1):
            results[i] *= right_product
            right_product *= nums[i]
        return results


# Example usage
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]
