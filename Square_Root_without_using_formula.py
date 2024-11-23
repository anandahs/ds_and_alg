def sqrt_root_easy(n):
    if n == 0 or n == 1:
        return n
    else:
        return int(n ** (1 / 2))


def binary_search(data, n):
    left, right = 0, len(data)-1

    while left <= right:
        mid = left + right // 2
        mid_data = data[mid]
        if mid_data == n:
            break
        elif mid_data > n:
            right = mid - 1
        elif mid_data < n:
            left = mid + 1
        if left == right:
            break;

    return mid


def sqrt_root(n):
    if n in [0, 1]:
        return n
    else:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2

            square = mid * mid

            if square == n:
                return mid
            if square > n:
                right = mid - 1
            elif square < n:
                left = mid + 1


if __name__ == "__main__":

    while True:
        try:
            n = int(input("input number that requires sqrt:"))
            print(f"sqrt_root_easy:{sqrt_root_easy(n)}")
            print(f"sqrt_root:{sqrt_root(n)}")

            data = [1, 2, 3, 4, 5, 6]
            search_item = 6
            print(f"Element {search_item} found at {binary_search(data, search_item)} location")

            break
        except ValueError as ex:
            print(f"please enter valid integer for sqrt calculation")
