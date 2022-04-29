import json

class TreeNode:
    def __init__(self,key,val,left=None,right=None, parent=None):
        self.key = key # number of node
        self.payload = val # string of sql query
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self



with open("./cache/tree/tree.json", "r") as file:
    f = json.load(file)






