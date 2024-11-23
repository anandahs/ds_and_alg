class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    # class LinkedList1:


#     def __init__(self, value):
#         new_node = Node(value)  # ---------- O(1)
#         self.head = new_node  # ---------- O(1)
#         self.tail = new_node  # ---------- O(1)
#         self.length = 1


class LinkedList:
    def __init__(self):
        self.head = None  # ---------- O(1)
        self.tail = None  # ---------- O(1)
        self.length = 0

    def __check_empty_list(self):
        return True if self.head is None else False

    def __initialize_empty_list(self, new_node):
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # time/space complexity of append is O(1)
    def append(self, value):
        new_node = Node(value)  # ------ O(1)

        if self.head is None:  # ------ O(1)
            self.head = new_node  # ------ O(1)
            self.tail = new_node  # ------ O(1)
        else:
            self.tail.next = new_node  # ------ O(1)
            self.tail = new_node  # ------ O(1)

        self.length += 1  # ------ O(1)

    # time/space complexity of prepend is O(1)
    def prepend(self, value):
        new_node = Node(value)  # ------ O(1)

        if self.head is None:  # ------ O(1)
            self.head = new_node  # ------ O(1)
            self.tail = new_node  # ------ O(1)
        else:
            new_node.next = self.head  # ------ O(1)
            self.head = new_node  # ------ O(1)

        self.length += 1  # ------ O(1)

    #                 40 ( new_node)
    # 10      30                      50     60
    #     temp_node
    # time complexity is O(n) whereas space complexity is O(1)
    def insert(self, index, value):

        if index >= self.length or index < 0:
            raise Exception(
                f"insert position {index} cannot be negative or  greater than linked list size {self.length}")

        if self.__check_empty_list():
            new_node = Node(value=value)
            self.__initialize_empty_list(new_node=new_node)

        else:

            if index == 0:
                self.prepend(value=value)
            else:
                new_node = Node(value=value)

                temp_node = self.head
                for _ in range(index - 1):  # 5  O(n) -  worst case scenario
                    temp_node = temp_node.next  # 0(1)
                new_node.next = temp_node.next  # 0(1)
                temp_node.next = new_node  # 0(1)
                self.length += 1  # 0(1)

    # time complexity is O(n) and space complexity is O(1) as there is no additional space consumed.
    def traverse(self):
        current_node = self.head  # O(1)
        while current_node:  # O(n)
            print(current_node.value, end=" ")  # O(1)
            current_node = current_node.next  # O(1)
        print()  # O(1)

    # time complexity of search is O(n), space complexity is O(1)
    def search(self, target):
        current_node = self.head  # O(1)
        index = 0  # O(1)
        while current_node:  # O(n)
            if target == current_node.value:  # O(n)
                return f"{target} is found at position {index + 1} in list:{self}"  # O(n)
            current_node = current_node.next  # O(1)
            index += 1  # O(n)

        return f"element {target} is not found in {self} "

    # time complexity of get method is O(n)
    # and space complexity is O(1) constant time complexity since space used does not change.
    def get(self, index):

        if self.head is None:
            return None

        if index == -1:
            return self.tail

        if index < -1 or index >= self.length:
            return None

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    # O(1) in space and time complexity
    def pop_first(self):

        if self.head is None:
            return None

        popped_node = self.head
        if popped_node.next:
            self.head = popped_node.next
            popped_node.next = None
        else:
            self.head = None
            self.tail = None
        self.length -= 1
        return popped_node

    # O(n) in time complexity and O(1) in time complexity
    def pop(self):

        if self.length == 0:
            return None
        popped_node = self.tail  # O(1)
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp_node = self.head  # O(1)
            while temp_node.next is not self.tail:  # O(n)
                temp_node = temp_node.next
            temp_node.next = None  # O(1)
            self.tail = temp_node  # O(1)
        self.length -= 1  # O(1)
        return popped_node  # O(1)

    def remove(self, index):
        popped_node = None
        if self.length == 0:
            return popped_node
        if index < 0 or index >= self.length:
            return popped_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next

            if temp_node.next is not self.tail:
                popped_node = temp_node.next
                temp_node.next = temp_node.next.next
            else:
                popped_node = self.pop()
            popped_node.next = None
            self.length -= 1
            return popped_node
        # time complexity is O(n)

    # space complexity is O(1)
    def set_value(self, index, value):
        if self.head is None and index == 0:
            node = Node(value=value)
            self.head = node
            self.tail = node

        temp_node = self.get(index)  # O(n)
        if temp_node:
            temp_node.value = value  # O(1)
            return True
        return False

    # time and space complexity is o(1)
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

     def remove_raw(self, index):

        popped_node = None

        if index < 0 or index >= self.length or self.length == 0:
            return popped_node

        if index == 0 and self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None

        else:

            temp_node = self.head

            for _ in range(index - 1):
                temp_node = temp_node.next

            if index == 0:
               self.head = temp_node.next
               popped_node = temp_node

            else:
                popped_node = temp_node.next

                if popped_node is self.tail:
                    temp_node.next = None
                    self.tail = temp_node
                else:
                    temp_node.next = temp_node.next.next

        self.length -= 1
        return popped_node

    def remove_instructor_implemented(self, index):
        if index < 0 or index >= self.length:
            return None

        # if node to be removed is the head nodes
        elif index == 0:
            popped_node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node

        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next

            popped_node = temp.next

            # if node to be removed is the tail node
            if popped_node.next is None:
                self.tail = temp

            temp.next = temp.next.next
            popped_node.next = None
            self.length -= 1
            return popped_node

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result


if __name__ == "__main__":
    try:
        linked_list = LinkedList()
        linked_list.append(10)
        linked_list.append(20)
        linked_list.append(45)
        linked_list.append(50)
        print("\n\n\n")
        print(f"Linked list after append :{linked_list}")
        print(f"head_value:{linked_list.head.value}")
        print(f"tail_value:{linked_list.tail.value}")
        linked_list.prepend(5)
        linked_list.prepend(2)
        print("\n\n\n")
        print(f"Linked list after prepend :{linked_list}")
        print(f"head_value:{linked_list.head.value}")
        print(f"tail_value:{linked_list.tail.value}")
        # linked_list.insert(6, 47)
        print(f"Linked list after insert 47:{linked_list}")
        print(f"head_value:{linked_list.head.value}")
        print(f"tail_value:{linked_list.tail.value}")
        linked_list.insert(1, 3)
        linked_list.insert(0, 1)
        print("\n\n\n")
        print(f"Linked list after insert :{linked_list}")
        print(f"head_value:{linked_list.head.value}")
        print(f"tail_value:{linked_list.tail.value}")

        # linked_list.insert(0, 1)
        # linked_list.insert(7, 47)
        # linked_list.insert(-1, 90)
        print(linked_list.length)
        print(linked_list)
        linked_list.traverse()
        print(linked_list.search(47))
        print(linked_list.search(20))
        print(linked_list.search(1))
        # print(linked_list.get(9))
        # print(linked_list.get(6))
        print(linked_list.get(1))
        print(linked_list.get(0))
        print(linked_list.get(6))
        print(linked_list.get(9))
        print(linked_list.set_value(9, 100))
        print(linked_list)
        print(linked_list.set_value(0, 2))
        print(linked_list)
        print(linked_list.set_value(8, 37))
        print("\n\n\n")
        print(f"Linked list after setvalue :{linked_list}")
        print(f"head_value:{linked_list.head.value}")
        print(f"tail_value:{linked_list.tail.value}")

        # for _ in range(12):
        #     print(f"popped_first_value:{linked_list.pop_first().value}")
        #     print(linked_list)
        #     print(f"linked list length:{linked_list.length} after pop_first")

        # for _ in range(12):
        #     popped_node = linked_list.pop()
        #     if popped_node is not None:
        #         print(f"popped_value:{popped_node.value}")
        #     else:
        #         print(f"No more data in linked list, it is empty:{linked_list}")
        #         break
        #     print(linked_list)
        #     print(f"linked list length:{linked_list.length} after pop")

        print(f"removed {linked_list.remove(3)} at index 3 from {linked_list}")
        print(f"head_value:{linked_list.head.value}")
        print(f"tail_value:{linked_list.tail.value}")
        print(f"removed {linked_list.remove(6)} at index 6 from {linked_list}")
        print(f"head_value:{linked_list.head.value}")
        print(f"tail_value:{linked_list.tail.value}")
        print(f"removed {linked_list.remove(0)} at index 0 from {linked_list}")
        print(f"head_value:{linked_list.head.value}")
        print(f"tail_value:{linked_list.tail.value}")
        linked_list.delete_all()
        print(f"linked_list:{linked_list} after deleting all")
    except Exception as e:
        print("Exception has occurred:" + str(e.with_traceback()))
        exit(101)
