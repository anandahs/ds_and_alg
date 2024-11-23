def max_value_key(my_dict):

    highest_key = 'dummy'
    highest_value = 0

    for key, value in my_dict.items():

        if value > highest_value:
            highest_value = value
            highest_key = key

    return highest_key

def max_value_key1(my_dict):
    return max(my_dict, key=my_dict.get)

if __name__ == "__main__":
    my_dict = {'a': 5, 'b': 9, 'c': 2}
    print(max_value_key(my_dict))
    print(max_value_key1(my_dict))
