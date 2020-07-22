
class Node:
    '''
    Define a binary Node object
    '''
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def Inorder(node):
    '''
    Prints a tree in order given the root node
    '''
    if node:
        Inorder(node.left)
        print(node.value)
        Inorder(node.right)

def Postorder(node):
    '''
    Prints a tree post order given the root node
    '''
    if node:
        Postorder(node.left)
        Postorder(node.right)
        print(node.value)

def Preorder(node):
    '''
    Prints a tree pre order given a root node
    '''
    if node:
        print(node.value)
        Preorder(node.left)
        Preorder(node.right)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Inorder tree traversal")
Inorder(root)

print ("Postorder tree traversal")
Postorder(root)

print ("Preorder tree traversal")
Preorder(root)

