from collections import Counter
import numpy as np


class ListOperations:
    def __init__(self):
        self.shopping_list = ['cloths', 'jewellery', 'milk', 'celery', 'kale']

    def list_string_slicing(self):

        name = 'Ananda'
        name_list = list(name)
        print(name_list)

        name1 = "Ananda-Harihara-Shivamurthy"
        name_list1 = name1.split("-")
        print(f"string split name_list1:{name_list1}")

        name2 = "Ananda Harihara Shivamurthy"
        name_list2 = name2.split()
        print(name_list2)
        print(f"string split name_list2:{name_list2}")

        name_list2_join = '-'.join(name_list2)
        print(f"name_list2_join:{name_list2_join}")

        name_list1_join = ' '.join(name_list1)
        print(f"name_list1_join:{name_list1_join}")

    def array_vs_list(self):

        # arrays and list
        # both are good for traversels and processing list of items

        # however, arrays are good for airthmetic operations and also it will always hold items of same type
        data = np.array([1, 2, 3, 4, 5])
        data1 = data / 5
        print(data1)

        list1 = [1, 2, 410, 54, 5]
        # this does not work
        # list11 = list1/5

        list2 = sorted(list1)
        print(f"original list:{list1}")
        print(list2)
        print(f"sorted list:{list2}")
        # sorts list since its mutable
        list1.sort()
        print(list1)

    def list_misc_operations(self):
        list1 = [1, 2, 3, 4]
        list2 = [10, 20, 30, 40]

        list3 = list1 + list2
        list4 = list1 * 2

        max_value = max(list4)
        min_value = min(list4)
        sum_value = sum(list4)
        length = len(list4)
        print(list3)
        print(list4)

        print(f"max_value:{max_value}")
        print(f"min_value:{min_value}")
        print(f"sum_value:{sum_value}")
        print(f"length:{length}")
        print(f"counter:{Counter(list2)}")

        for key, value in Counter(list2).items():
            print(f"key:{key} value:{value}")

        print(f"zipped:{zip(list1, list2)}")

        zipped = list(zip(list1, list2))
        print(zipped)

        data = list()
        print(f"length:{len(data)}")

        if 4 in list1:
            print(f"4 is found")

        if 30 in list1:
            print(f"30 is found")
        else:
            print(f"30 is not found")

    def perform_list_insert_operations(self):
        print("List insert has 3 operations -> append, insert and extend")
        self.shopping_list = ['cloths', 'jewellery', 'milk', 'celery', 'kale']
        print(f"original list:{self.shopping_list}")
        additional_items = ['plants', 'torch']
        self.shopping_list.append('car')
        print(f"list post append:{self.shopping_list}")
        self.shopping_list.insert(0, 'glass')
        print(f"list post insert:{self.shopping_list}")
        self.shopping_list.extend(additional_items)
        print(f"list post extend:{self.shopping_list}")
        print("\n")

    def perform_list_delete_operations(self):
        print("List insert has 3 operations -> pop, remove and delete")
        self.shopping_list = ['cloths', 'jewellery', 'milk', 'celery', 'kale']
        print(f"original list:{self.shopping_list}")
        self.shopping_list.pop(0)
        print(f"list post pop by index at 0:{self.shopping_list}")
        self.shopping_list.pop()
        print(f"list post pop(), deleted element at end:{self.shopping_list}")
        self.shopping_list.remove('jewellery')
        print(f"list delete item by value not by index:{self.shopping_list}")
        print("\n")

    def perform_list_slice_operations(self):
        print("List slice operations, very handy")
        self.shopping_list = ['cloths', 'jewellery', 'milk', 'celery', 'kale']
        print(f"slice1:{self.shopping_list[::-1]}")
        print(f"slice2:{self.shopping_list[:-1]}")
        print(f"slice3:{self.shopping_list[:-2]}")
        print(f"slice4:{self.shopping_list[:]}")
        print(f"slice5:{self.shopping_list[::2]}")
        print(f"slice5:{self.shopping_list[-5:-2:2]}")
        print(f"slice6:{self.shopping_list[-5:-2]}")


if __name__ == "__main__":
    listOperation = ListOperations()
    # listOperation.perform_list_insert_operations()
    # listOperation.perform_list_delete_operations()
    # listOperation.perform_list_slice_operations()
    # listOperation.list_misc_operations()
    # listOperation.list_string_slicing()
    listOperation.array_vs_list()
