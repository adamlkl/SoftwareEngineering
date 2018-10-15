from collections import defaultdict
from queue import Queue


class Digraph:
    
    def __init__(self, vertices, edges):
        self.V = int(vertices)
        self.E = int(edges)
        self.edges = 0
        self.digraph = defaultdict(list)

        for v in range(self.V):
            self.digraph[v].append(0)
            self.digraph[v].pop(0)

        self.indegree = [0] * self.V
        self.marked = [False] * self.V
        self.edgeTo = [-1] * self.V

    def add_vertex(self, v, adj):
        if self.validate_vertex(v) and self.validate_vertex(adj):
            self.digraph[v].append(adj)
            self.indegree[adj] += 1
            self.edges += 1

    def check_vertex(self):
        if self.V != len(self.digraph):
            self.V = len(self.digraph)

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
        self.check_vertex()
        visit = [False] * self.V
        remarked = [False] * self.V
        for v in range(self.V):
            if visit[v] is False:
                if self.__check_cyclic(v, visit, remarked):
                    return True
        return False
    
    def __check_cyclic(self, v, visit, remarked):
        visit[v] = True
        remarked[v] = True
        
        for w in self.digraph[v]:
            if visit[w] is False:
                if self.__check_cyclic(w, visit, remarked) is True:
                    return True
            elif visit[w] is True and remarked[w] is True:
                return True
        
        remarked[v] = False
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
        self.check_vertex()
        if self.check_cyclic():
            return -1

        if self.haspathto(v) and self.haspathto(w):
            path1 = self.pathto(v, root)
            path2 = self.pathto(w, root)
            p1 = path1.get()
            p2 = path2.get()
            if path1.empty() or path2.empty():
                if p1 == p2:
                    return p1
                else:
                    return -3

            else:
                while not path1.empty() or not path2.empty():
                    if path1.qsize() > path2.qsize():
                        p1 = path1.get()
                    elif path2.qsize() > path1.qsize():
                        p2 = path2.get()
                    else:
                        p1 = path1.get()
                        p2 = path2.get()

                    if p1 == p2:
                        return p1

                return -3

        else:
            return -2

    def arrangedepth(self, walk, dst):
        newwalk = defaultdict(list)
        depthlevel = 0
        for y in walk:
            self.validate_vertex(y)
            newwalk[depthlevel].append(y)
            if y != dst:
                depthlevel += 1
            else:
                depthlevel = 0
        return newwalk

    def compute_lca2(self, root, v, w):
        walk = self.find_all_paths(root, v)
        walk.reverse()
        newwalk = self.arrangedepth(walk, root)
        walk2 = self.find_all_paths(root, w)
        walk2.reverse()
        newwalk2 = self.arrangedepth(walk2, root)

        if len(newwalk) > len(newwalk2):
            index = len(newwalk) - len(newwalk2)
            for x in range(len(newwalk2)):
                if self.intersect(newwalk[index], newwalk2[x]):
                    return self.intersect(newwalk[index], newwalk2[x])
                index += 1

        elif len(newwalk) < len(newwalk2):
            index = len(newwalk2) - len(newwalk)
            for x in range(len(newwalk)):
                if self.intersect(newwalk[x], newwalk2[index]):
                    return self.intersect(newwalk[x], newwalk2[index])
                index += 1

        else:
            for x in range(len(newwalk)):
                if self.intersect(newwalk[x], newwalk2[x]):
                    return self.intersect(newwalk[x], newwalk2[x])

    '''A recursive function to find all paths from 'u' to 'd'. 
           visited[] keeps track of vertices in current path. 
           path[] stores actual vertices and path_index is current 
           index in path[]'''

    def __find_all_paths_util(self, u, d, visited, path, walk):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then find
        # current path[]
        if u == d:
            walk.extend(path)

        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.digraph[u]:
                if visited[i] is False:
                    self.__find_all_paths_util(i, d, visited, path, walk)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # finds all paths from 's' to 'd'
    def find_all_paths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * self.V
        walk = list()

        # Create an array to store paths
        path = []

        # Call the recursive helper function to find all paths
        self.__find_all_paths_util(s, d, visited, path, walk)
        return walk

    def print_digraph(self):
        return self.digraph

    @staticmethod
    def intersect(a, b):
        return list(set(a) & set(b))
