
import json


class TreeNode:
    def __init__(self,key,val,level,left=None,right=None, parent=None):
        self.key = key # number of node
        self.level = level # boolean, "0" or "1"
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
    
    values = binaryTreePaths(node_00)
    keys = binaryTreeBooleanPaths(node_00)

    res = {keys[i]:values[i] for i in range(len(keys))}

    return res


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
# level0
node_00 = TreeNode(0, query0, '0')
# level1
node_01 = TreeNode(1, query10, '0')
node_02 = TreeNode(2, query11, '1')
node_03 = TreeNode(3, query20, '0')
node_04 = TreeNode(4, query21, '1')
node_05 = TreeNode(5, query20, '0')
node_06 = TreeNode(6, query21, '1')
# level2
node_07 = TreeNode(7, query30, '0')
node_08 = TreeNode(8, query31, '1')
node_09 = TreeNode(9, query30, '0' )
node_10 = TreeNode(10, query31, '1')
node_11 = TreeNode(11, query30, '0')
node_12 = TreeNode(12, query31, '1')
node_13 = TreeNode(13, query30, '0')
node_14 = TreeNode(14, query31, '1')
# build tree
node_00.leftChild = node_01
node_00.rightChild = node_02
node_01.leftChild = node_03
node_01.rightChild = node_04
node_02.leftChild = node_05
node_02.rightChild = node_06
node_03.leftChild = node_07
node_03.rightChild = node_08
node_04.leftChild = node_09
node_04.rightChild = node_10
node_05.leftChild = node_11
node_05.rightChild = node_12
node_06.leftChild = node_13
node_06.rightChild = node_14

node_01.parent = node_00
node_02.parent = node_00
node_03.parent = node_01
node_04.parent = node_01
node_05.parent = node_02
node_06.parent = node_02
node_07.parent = node_03
node_08.parent = node_03
node_09.parent = node_04
node_10.parent = node_04
node_11.parent = node_05
node_12.parent = node_05
node_13.parent = node_06
node_14.parent = node_06





def tree_to_dict(root):
    """write decision tree to json format

    Parameters
    ----------
    root: Class TreeNode object

    Returns
    -------
    dictionary
    """

    dict = {}
    dict["node"] = root.key
    dict["content"] = root.payload
    
    if not root.isLeaf():
        dict["leftNode"] = tree_to_dict(root.leftChild)
    else:
        dict["leftNode"] = None
    
    if not root.isLeaf():
        dict["rightNode"] = tree_to_dict(root.rightChild)
    else:
        dict["rightNode"] = None

    return dict

def tree_to_json():
    with open("./cache/tree/tree.json", "w") as outfile:
        json.dump(tree_to_dict(node_00), outfile)


