
class BinaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def add(self, value):
        pass


pre_order=[]
in_order=[]
post_order=[]
def BSTTraversal(node):
    if node is None:
        return
    
    global pre_order
    pre_order.append(node.value)

    BSTTraversal(node.left)

    global in_order
    in_order.append(node.value)
    
    BSTTraversal(node.right)

    global post_order
    post_order.append(node.value)




def test():
    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.right = BinaryTree(15)
    root.left.left = BinaryTree(1)
    root.left.right = BinaryTree(7)
    root.right.left = BinaryTree(13)
    root.right.right = BinaryTree(18)


    sums = BSTTraversal(root)
    print(pre_order)
    print(in_order)
    print(post_order)


test()