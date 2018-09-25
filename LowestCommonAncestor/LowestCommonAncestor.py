#LowestCommonAncestor
class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class LCA:

    size = 0
    root = None

    def __init__(self,val):
        self.root = TreeNode(val)
        self.size += 1

    def isempty(self):
        return self.root is None

    def __sizeof__(self):
        return self.size

    #TODO
    def insert(self,data):
        if data is None:
            return False
        else:
            self.__insert(self.root,data)
            return True

    def __insert(self, node, data):
        if node.data:
            if node.data > data:
                if node.left is None:
                    node.left = TreeNode(data)
                    self.size += 1
                else:
                    self.__insert(node.left, data)
            elif node.data < data:
                if node.left is None:
                    node.right = TreeNode(data)
                    self.size += 1
                else:
                    self.__insert(node.right,data)
        else:
            node.data=data


    # Returns LCA if node a , b are present in the given
    # binary tre otherwise return -1
    def findlca(self,a, b):

        if self.isEmpty(): return False
        # To store paths to a and b from the root
        path1 = []
        path2 = []

        # Find paths from root to a and root to b.
        # If either a or b is not present , return -1
        if not self.__findpath(self.root, path1, a) or not self.__findpath(self.root, path2, b):
            return -1

            # Compare the paths to get the first different value
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i - 1]

    def __findpath(self, node, path, k):
        if node is None:
            return False

        path.append(node.data)

        if node.data == k:
            return True

        if (node.left is None and self.__findpath(node.left, path, k)) or (node.right is None and self.__findpath(node.right, path, k)):
            return True

        path.pop()
        return False








