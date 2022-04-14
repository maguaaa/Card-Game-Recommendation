

class TreeNode:
    def __init__(self,key,val,level,left=None,right=None, parent=None):
        self.key = key
        self.level = level
        self.payload = val
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




class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def put(self,key,val,level):
        if self.root:
            self._put(key,val,level,self.root)
        else:
            self.root = TreeNode(key,val,level)
        self.size = self.size + 1

    def _put(self,key,val,level,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,level,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,level,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,level,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,level,parent=currentNode)






def binaryTreePaths(root):
    """find all paths from root to leaf

    Parameters
    ----------
    root: Class TreeNode
        root node

    Returns
    -------
    res: a list of all paths
    """
    if not root:
        return []

    stack = [root]
    stackPath = []
    res = []
    stackPath.append(root.payload)

    while stack:

        node = stack.pop()
        path = stackPath.pop()

        if node.isLeaf():
            res.append(path)

        if node.rightChild:
            stack.append(node.rightChild)
            stackPath.append(path + node.rightChild.payload)

        if node.leftChild:
            stack.append(node.leftChild)
            stackPath.append(path + node.leftChild.payload)

    return res


def binaryTreeBooleanPaths(root):
    """find all paths from root to leaf

    Parameters
    ----------
    root: Class TreeNode
        root node

    Returns
    -------
    res: a list of all paths
        every item has only 3 digits, only composed of 0 or 1; 0:=no, 1:=yes
    """
    if not root:
        return []

    stack = [root]
    stackPath = []
    res = []
    stackPath.append(root.level)

    while stack:

        node = stack.pop()
        path = stackPath.pop()

        if node.isLeaf():
            res.append(path[1:])

        if node.rightChild:
            stack.append(node.rightChild)
            stackPath.append(path + node.rightChild.level)

        if node.leftChild:
            stack.append(node.leftChild)
            stackPath.append(path + node.leftChild.level)

    return res


def buildDecisionTree():
    """build decision dict

    Parameters
    ----------
    None

    Returns
    -------
    dict
        key:binary string path, value:query string
    """
    query0 = '''
    select distinct t1.*
    from'''

    query10 = '''
    (select *
        from games
    where metacritic is null
    )t1'''

    query11 = '''
    (select *
        from games
    where metacritic is not null
    )t1'''

    query20 = '''
    where t1.id not in
        (select distinct id
            from games_platforms
        where platform_id in
            (select id
                from platforms 
            where name in ('PlayStation','Xbox','Nintendo','SEGA'))
        )'''

    query21 = '''
    where t1.id in
        (select distinct id
            from games_platforms
        where platform_id in
            (select id
                from platforms 
            where name in ('PlayStation','Xbox','Nintendo','SEGA'))
        )'''

    query30 = '''
    and t1.id not in
        (select distinct id
            from games_tags 
        where tag_id in 
            (select id
                from tags
            where name like '%solitaire%' 
            or name like '%single%')
        )
    order by t1.rating desc'''

    query31 = '''
    and t1.id in
        (select distinct id
            from games_tags 
        where tag_id in 
            (select id
                from tags
            where name like '%solitaire%' 
            or name like '%single%')
        )
    order by t1.rating desc'''    
    nodelist=[(55, query0, '0'),(40, query10, '0'),(83, query11, '1'),(35, query20, '0'),(51, query21, '1'),(80, query20, '0'),(85, query21, '1'),(17, query30, '0'),(37, query31, '1'),(50, query30, '0'),(52, query31, '1'),(70, query30, '0'),(81, query31, '1'),(84, query30, '0'),(100, query31, '1')]
    tree = BinarySearchTree()
    for k, v, l in nodelist:
        tree.put(k,v,l)

    values = binaryTreePaths(tree.root)
    keys = binaryTreeBooleanPaths(tree.root)

    res = {keys[i]:values[i] for i in range(len(keys))}

    return res




