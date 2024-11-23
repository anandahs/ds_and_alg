class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_leaf(node):
    if node.left is None and node.right is None:
        return True


def left_sum_of_tree(tree_root):
    if tree_root is None:
        return 0

    left_sum = 0

    if tree_root.left and is_leaf(tree_root.left):
        left_sum += tree_root.left.value

    left_sum += left_sum_of_tree(tree_root.left)
    left_sum += left_sum_of_tree(tree_root.right)

    return left_sum


if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7]

    # next_node = 3
    # print(next_node)
    # root_node = Tree(0)
    # tree_length = len(root)
    # print(tree_length)
    # tree_index = 0
    # while (tree_index < (tree_length - 1)):
    #     root_node = Tree(root[tree_index])
    #     if root.is True:

    tree_root = Tree(3)
    tree_root.left = Tree(9)
    tree_root.right = Tree(20)
    tree_root.right.left = Tree(15)
    tree_root.right.right = Tree(7)

    print(left_sum_of_tree(tree_root))

# for index, node in enumerate(root):
#     if index != 0 and index % next_node == 0:
#
#     else:
#         root = Tree(node)
