class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove(self, index):

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


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.remove(0)


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.remove(0)
    print(linked_list)
