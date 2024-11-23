data = []
data1 = list()

print(f"list1:{data}")
print(f"list2:{data1}")

english_to_kannada_dict1_empty = dict()
english_to_kannada_dict2_empty = {}

print(f"empty_dictionary1:{english_to_kannada_dict1_empty}")
print(f"empty_dictionary1:{english_to_kannada_dict2_empty}")

english_to_kannada_dict1 = dict(one="ondu", two="yeradu", three="mooru")
english_to_kannada_dict2 = {'one': "ondu", 'two': "yeradu", 'three': "mooru"}
dictionary_3 = [('one', 'ondu'), ('two', 'yeradu'), ('three', 'mooru')]
english_to_kannada_dict3 = dict(dictionary_3)

print(f"dictionary1:{english_to_kannada_dict1}")
print(f"dictionary2:{english_to_kannada_dict2}")
print(f"dictionary3:{english_to_kannada_dict3}")

mydict = {'Name': 'Ananda', 'Location': 'boston'}
mydict['Location'] = 'marlborough'
mydict['Age'] = 10

print(f"mydict:{mydict}")


def traverse_dict(dict):
    # time complexity O(n), space complexity is O(1) since extra space is not required.
    for key in dict:  # O(n)
        print(key, dict[key])  # O(1)


def search_dict(dict, value):
    # O(n), space complexity is O(1) since extra memory is not required for operation
    for key in dict:  # O(n)
        if dict[key] == value:  # O(1)
            return key, value  # O(1)
    return 'value not found in dict'  # O(1)


print(search_dict(mydict, 10))
print(search_dict(mydict, 23))

traverse_dict(mydict)


def delete_operations():
    print("All about delete operations in dictionary")

    my_dict1 = {'Name': 'Ananda', 'Location': 'marlborough', 'Age': 10}

    del my_dict1['Name']  # O(1) for time, O(1) for space complexity since additional memory is not required
    print(f"my_dict1 after del:{my_dict1}")

    my_dict1['name'] = 'Ananda'

    print(my_dict1)

    deleted_element = my_dict1.pop(
        'name')  # O(1) for time, O(1) for space complexity since additional memory is not required
    deleted_element2 = my_dict1.popitem()  # O(1) for time, O(1) for space complexity since additional memory is not required

    print(f"pop:{deleted_element}")
    print(f"pop_element:{deleted_element2}")

    print(f"dictionary after two pops:{my_dict1}")

    my_dict1['name'] = 'Ananda'
    my_dict1['Age'] = 'Ananda'

    my_dict1.clear()  # time complexity is O(n) -  to delete all elements, space complexity is O(1) since additional memory is not required.

    print(f"dictionary after clear:{my_dict1}")


# copy, he says shallow copy, he is correct. it creates only new dictionary but does not copy underlying elements recursively.
# get(key, value) , value is default value, check by providing key that does not exist.
# items() methods, it returns keys and values tuple pairs
# keys(), list of keys, it's a view object
# values(), list of values, it's again a view object.
# popitem() , returns arbitrary element from dictionary , it returns pair that is removed.
# setdefault(key, value), it returns value if key exists, else it will insert key with value.
# pop(key, defaultValue), it returns removes and gives element, pop('name1', 'not'),
# update(other_dictionary or tuple), pass another dictionary to insert/update. it will insert if keys does not exist, insert if keys does not exist
def dict_operations():
    print("All about dictionary operations")

    my_dict1 = {'Name': 'Ananda', 'Location': 'marlborough', 'Age': 10, 'gadgets': [10, 20, 30]}

    # does shallow copy
    my_dict2 = my_dict1.copy()

    my_dict2['Location'] = 'Quincy'
    my_dict2['gadgets'].append('40')
    print(f"my_dict1 post shallow copy:{my_dict1}")
    print(f"my_dict2 post shallow copy:{my_dict2}")

    # get , default or new value
    value1 = my_dict1.get('Name1', 'Rajanna')
    value2 = my_dict1.get('Name')

    print(f"value1:{value1}")
    print(f"value1:{value2}")

    # items, keys and values
    for key, value in my_dict1.items():
        print(f"key:{key} value:{value}")

    my_dict1_values = my_dict1.values()

    print(f"my_dict1_values:{my_dict1_values}")

    my_dict1_keys = my_dict1.keys()

    print(f"my_dict1_keys:{my_dict1_keys}")

    # popitem() , returns arbitrary element from dictionary , it returns pair that is removed.

    item_removed = my_dict1.popitem()

    print(f"item_removed:{item_removed}")

    print(f"my_dict1 after popitem:{my_dict1}")

    # setdefault(key, value), it returns value if key exists, else it will insert key with value.

    my_dict1.setdefault('Name', 'Shiva')
    my_dict1.setdefault('Education', 'BE')

    print(f"my_dict post setdefault:{my_dict1}")

    # fromKeys

    my_dict2 = my_dict1.fromkeys(('wife', 'language'), ('chethana', 'kannada'))

    print(f"my_dict1 post fromkeys:{my_dict1}")
    print(f"my_dict2 post fromkeys:{my_dict2}")

    dictionary_3 = [('one', 'ondu'), ('two', 'yeradu'), ('three', 'mooru')]
    english_to_kannada_dict3 = dict(dictionary_3)
    print(english_to_kannada_dict3)

    # pop(key, defaultValue), it returns removes and gives element, pop('name1', 'not'),

    popped_data1 = english_to_kannada_dict3.pop('one', 'onda')
    popped_data2 = english_to_kannada_dict3.pop('four', 'nalka')

    print(f"popped_data1={popped_data1}")
    print(f"popped_data2={popped_data2}")

    print(f"dictionary_3:{english_to_kannada_dict3}")

    # update(other_dictionary or tuple), pass another dictionary to insert/update. it will insert if keys does not exist, insert if keys does not exist
    dictionary_5 = [('one', 'ondu'), ('two', 'Varudu'), ('three', 'mooru')]
    english_to_kannada_dict3.update(dictionary_5)

    print(f"english_to_kannada_dict3 post update:{english_to_kannada_dict3}")


def dict_operations_2():
    dict1 = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
    dict2 = {1: "one", False: "two", 3: "three", 4: "four", 5: "five"}
    dict3 = {False: "one", False: "two", False: "three", False: "four", False: "five"}

    print(1 in dict1)
    print("one" in dict1.values())
    print(any(dict1))
    print(all(dict1))
    print(all(dict2))
    print(any(dict3))
    print(sorted(dict1))


dict_operations()
dict_operations_2()
# delete_operations()
