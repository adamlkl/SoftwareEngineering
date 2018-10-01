"""#create a Node class for the binary tree"""


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


'#LCA class: creates a binary tree that includes basic functions of the tree and performs LCA'


class LCA:
    def __init__(self):
        self.size = 0
        self.root = None

    '#TODO public boolean isEmpty ()'
    '#return if the tree is empty namely size is 0'
    def isempty(self):
        return self.root is None

    '#TODO public int size'
    '#return siz of tree'
    def __size__(self):
        return self.size

    '#TODO public boolean insert (data)'
    '#returns true if insert data successfully, otherwise false'
    def insert(self, data):
        if data is None or type(data) is not int:
            return False
        elif self.root is None:
            self.root = TreeNode(data)
            self.size += 1
            return True
        else:
            self.__insert(self.root, data)
            return True

    '#TODO public boolean insert (node, data)'
    '#insert a data into the tree, creates a new node if there are no duplicates of the data in the tree.'
    def __insert(self, node, data):
        if node.data:
            if node.data > data:
                if node.left is None:
                    node.left = TreeNode(data)
                    self.size += 1
                else:
                    self.__insert(node.left, data)
            elif node.data < data:
                if node.right is None:
                    node.right = TreeNode(data)
                    self.size += 1
                else:
                    self.__insert(node.right, data)
        else:
            node.data = data

    '# TODO public boolean findLCA (int a, int b)'
    '# Returns LCA if node a , b are present in the given'
    '# binary tre otherwise return -1'
    def findlca(self, a, b):
        if self.isempty():
            return False

        if type(a) is not int or type(b) is not int:
            return False

        '# To store paths to a and b from the root'
        path1 = []
        path2 = []

        '# Find paths from root to a and root to b.'
        '# If either a or b is not present , return -1'
        if not self.__findpath(self.root, path1, a) or not self.__findpath(self.root, path2, b):
            return -1

        '# Compare the paths to get the first different value'
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i - 1]

    '#TODO private boolean findPath (TreeNode node, int k)'
    '#check the whole tree for the data and append the path into a list'
    '#returns True if path found, otherwise return False'
    def __findpath(self, node, path, k):
        if node is None:
            return False

        path.append(node.data)

        if node.data == k:
            return True

        if (node.left is not None and self.__findpath(node.left, path, k)) or \
                (node.right is not None and self.__findpath(node.right, path, k)):
            return True

        path.pop()
        return False
