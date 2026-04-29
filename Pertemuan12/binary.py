class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)
        return self.root

    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node
        return parent_node.left

    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node
        return parent_node.right

tree = BinaryTree()

F = tree.insert_root("F")

B = tree.insert_left(F, "B")
G = tree.insert_right(F, "G")

A = tree.insert_left(B, "A")
D = tree.insert_right(B, "D")

I = tree.insert_right(G, "I")

C = tree.insert_left(D, "C")
E = tree.insert_right(D, "E")

H = tree.insert_left(I, "H")

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

print("Preorder:")
preorder(tree.root)

print("\nInorder:")
inorder(tree.root)

print("\nPostorder:")
postorder(tree.root)