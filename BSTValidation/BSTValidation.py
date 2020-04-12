
class BinaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def add(self, value):
        pass


def validateBST(root):
    return validateNode(root, float("-inf"), float("inf"), None)

is_valid = True
# def validateNode(node, min_val, max_val):
#     if node is None:
#         return True

#     if node.value <= min_val or node.value > max_val:
#         return False

#     is_valid = validateNode(node.left, min_val, node.value)
#     return is_valid and validateNode(node.right, node.value, max_val)

# def validateNode(node, min_val, max_val):
#     if node is None:
#         return

#     if node.value <= min_val or node.value > max_val:
#         global is_valid
#         is_valid = False
#         return 

#     validateNode(node.left, min_val, node.value)
#     validateNode(node.right, node.value, max_val)

def validateNode(node, min_val, max_val, parent_node):
    # if node is None:
    #     if parent_node.value == 1:
    #         return True
    #     return False
    if node is None:
        return False
    validateNode(node.left, min_val, node.value, node)
    validateNode(node.right, node.value, max_val, node)


def test():
    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.right = BinaryTree(15)
    root.left.left = BinaryTree(1)
    root.left.right = BinaryTree(7)
    root.right.left = BinaryTree(13)
    root.right.right = BinaryTree(18)


    sums = validateBST(root)
    print(sums)


test()