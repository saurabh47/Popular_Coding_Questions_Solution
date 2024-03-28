# Program to find depth or height of a tree
# A height of the tree is the number of vertices in the tree from the root to the deepest node. 

#           1
#         /   \
#        2     3
#       / \   / \
#      4   5 6   7
#     / \
#    8   9
#
#  Consider the above tree, the height of the tree is 4.

# Define a class Node with data, left, and right attributes.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def hasChild(self):
        return self.left != None or self.right != None
    def hasLeftChild(self):
        return self.left != None

    def hasRightChild(self):
        return self.right != None



# Define a class Tree with root attribute.
class Tree:
    def __init (self):
        self.root = None

    def findDepth(self, node):
        if node == None:
            return 0
        leftDepth = self.findDepth(node.left)
        rightDepth = self.findDepth(node.right)
        return max(leftDepth, rightDepth) + 1

if __name__ == '__main__':
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.left.left.left = Node(8)
    tree.root.left.left.right = Node(9)
    print(tree.findDepth(tree.root)) # 4

