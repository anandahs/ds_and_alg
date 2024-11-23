def needle_in_hay_stack(haystack, needle):
    h_len = len(haystack)
    n_len = len(needle)

    for i in range(h_len):
        j = 0
        for k in range(i, h_len):
            if haystack[k] == needle[j]:
                j += 1
            else:
                break

            if j == n_len:
                return i

    return -1


if __name__ == "__main__":
    haystack1 = "Ananda Harihara Shivamurthy"

    haystack2 = "Ananda Harihara Shivamurthy Chethana Hanumanthappa Yereshimi"
    print(needle_in_hay_stack(haystack1, 'Harihara'))
    print(needle_in_hay_stack(haystack2, 'Chethana'))
    print(needle_in_hay_stack(haystack2, 'Yereshimi'))
    print(needle_in_hay_stack(haystack2, 'Atharva'))
