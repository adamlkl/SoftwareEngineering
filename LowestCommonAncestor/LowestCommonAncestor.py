from collections import defaultdict
from queue import Queue


class Digraph:
    
    def __init__(self, vertices, edges):
        self.V = int(vertices)
        self.E = int(edges)
        self.digraph = defaultdict(list)
        self.indegree = [0] * self.V
        self.marked = [False] * self.V
        self.edgeTo = [-1] * self.V
    
    def add_vertex(self, v, adj):
        if self.validate_vertex(v) and self.validate_vertex(adj):
            self.digraph[v].append(adj)
            self.indegree[adj] += 1

    def indegree(self, v):
        return self.indegree[v]
    
    def incidence(self, v):
        return self.digraph[v]
    
    def find_root(self):
        roots = []
        for index in range(len(self.indegree)):
            if self.indegree[index] is 0:
                roots.append(index)
        return roots
    
    def validate_vertex(self, v):
        return (type(v) is int) and (v >= 0) and (v < self.V)
    
    def check_cyclic(self):
        visit = [False] * self.V
        remarked = [False] * self.V
        for v in range(self.V):
            if visit[v] is False:
                if self.__check_cyclic(v, visit, remarked) is True:
                    return True
        return False
    
    def __check_cyclic(self, v, visit, remarked):
        visit[v] = True
        remarked[v] = True
        
        for w in self.digraph[v]:
            if visit[w] is False:
                return self.__check_cyclic(w, visit, remarked)
            elif visit[w] is True and remarked[w] is True:
                return True
        
        remarked[v] = True
        return False

    def get_vertex(self):
        return self.V
    
    def get_edge(self):
        return self.E
    
    def bfs(self, s):
        q = Queue()
        self.marked[s] = True
        q.put(s)
        while not q.empty():
            v = q.get()
            for dst in self.digraph[v]:
                if self.marked[dst] is False:
                    self.edgeTo[dst] = v
                    self.marked[dst] = True
                    q.put(dst)

    def haspathto(self, v):
        self.validate_vertex(v)
        return self.marked[v]
    
    def pathto(self, v, root):
        self.validate_vertex(v)
        if not self.haspathto(v):
            return None
        q = Queue()
        dest = v
        while dest != root:
            q.put(dest)
            dest = self.edgeTo[dest]
        q.put(root)
        return q
    
    def compute_lowest_common_ancestor(self, v, w, root):
        self.bfs(root)
        if self.haspathto(v) and self.haspathto(w):
            path1 = self.pathto(v, root)
            path2 = self.pathto(w, root)
            
            while not path1.empty() or not path2.empty():
                p1 = path1.get()
                p2 = path2.get()
                if p1 == p2:
                    return p1
            return 100
        
        else:
            return -1

    def print_digraph(self):
        return self.digraph


file_x = open("tinyDAG.txt", "r")
vn = int(file_x.readline())
en = int(file_x.readline())
test = Digraph(vn, en)

for x in file_x:
    test.add_vertex(int(x.split(" ")[0]), int(x.split(" ")[1]))
print(test.compute_lowest_common_ancestor(1, 6, 2))
print(test.compute_lowest_common_ancestor(11, 10, 2))
print(test.compute_lowest_common_ancestor(6, 9, 2))
