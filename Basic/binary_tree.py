class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Search the tree
    def SearchTree(self,x):
        if x == self.data:
            return True
        elif self.data < x:
            if self.right:
                return self.right.SearchTree(x)
            else:
                return False
        else:
            if self.left:
                return self.left.SearchTree(x)
            else:
                return False

    def FindMin(self):
        if self.left is None:
            return self.data
        else:
            return self.left.FindMin()
    
    def FindMax(self):
        if self.right is None:
            return self.data
        else:
            return self.right.FindMin()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()
print(str(root.SearchTree(3)))
print(str(root.FindMin()))
print(str(root.FindMax()))