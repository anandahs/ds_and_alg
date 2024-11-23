# time complexity : O(1) + O(n) + O(1) = O(n)

def find_biggest(input):
    big_no = input[0]  # -------O(1)
    for i in range(1, len(input)):  # O(n)
        if input[i] > big_no:  # O(1)
            big_no = input[i]  # O(1)
    return big_no  # O(1)


if __name__ == '__main__':
    input = [1, 8, 10, 7, 6, 5]  # -------O(1)
    biggest_number = find_biggest(input)  # -------O(1)
    print(f"Biggest Number:{biggest_number}")  # -------O(1)
