class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = root

    def preorder(self, n):
        if n != None:
            print(n.data, '',end="")
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

# Test code
root = Node(5, Node(2, Node(7, Node(4), Node(1)), Node(3)), Node(9, Node(6), Node(10)))
tree = Tree(root)
tree.preorder(tree.root)
