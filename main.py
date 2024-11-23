from benjamin.list_operations import get_odd_list1, get_odd_list2

# This is a sample Python script.

# Press Alt+Shift+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+Shift+B to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    my_list = [1, 2, 3, 4, 5]
    odd_list1 = get_odd_list1(my_list)
    print(f"odd_list1:{odd_list1}")
    odd_list2 = get_odd_list2(my_list)
    print(f"odd_list2:{odd_list2}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
