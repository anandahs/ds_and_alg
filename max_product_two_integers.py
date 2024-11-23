import array


def max_products(array1):
    max1 = 0
    max2 = 0

    for num in array1:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    print(f"two max numbers are {max1} {max2}")
    return max1 * max2


array1 = array.array("i", [1, 2, 31, 4, 5, 6, 7, 8, 9])
print(array1)

print(max_products(array1))
