from collections import defaultdict
from queue import Queue


class Digraph:

    '''constructor of Digraph class. Digraph is stored in the default dict data tyoe.
    variables in Digraph: V(number of vertices),
                          E(number of edges)
                          indgree(number of vertices incident to one vertex)
                          marked(vertices that can be reached by root)
                          edgeTo(stores all the direct edges of all vertices when doing bfs'''
    def __init__(self, vertices, edges):
        self.V = int(vertices)
        self.E = int(edges)
        self.digraph = defaultdict(list)

        for v in range(self.V):
            self.digraph[v].append(0)
            self.digraph[v].pop(0)

        self.indegree = [0] * self.V
        self.marked = [False] * self.V
        self.edgeTo = [-1] * self.V

    '''Function: public void add_vertex
       Parameters: int vertex, int adjacent 
       Description: connect two edges in a digraph
       returns: --'''
    def add_vertex(self, v, adj):
        if self.validate_vertex(v) and self.validate_vertex(adj):
            self.digraph[v].append(adj)
            self.indegree[adj] += 1

    '''Function: public void check_vertex
       Parameters: --
       Description: correct the number of of vertices in the digraph
       returns: --'''
    def check_vertex(self):
        if self.V != len(self.digraph):
            self.V = len(self.digraph)

    '''Function: public int indegree
       Parameters: int vertex
       Description: returns the indegree of a certain vertex, otherwise 
                    return None If vertex not available in digraph. 
       returns: int indegree[v] / None'''
    def indegree(self, v):
        if self.validate_vertex(v):
            return self.indegree[v]
        else:
            return None

    '''Function: public int [] incidence
       Parameters: int vertex
       Description: returns the vertices incident to a certain vertex, 
                    otherwise return None if vertex not available in 
                    digraph. 
       returns: int [] digraph[v] / None'''
    def incidence(self, v):
        if self.validate_vertex(v):
            return self.digraph[v]
        else:
            return None

    '''Function: public int [] find_root
       Parameters: --
       Description: returns the root of the digraph stored in an int 
                    array, if there are no roots, then return an empty 
                    array. The roots are the vertices that do not have 
                    any vertex incident to it. 
       returns: int [] roots'''
    def find_root(self):
        roots = []
        for index in range(len(self.indegree)):
            if self.indegree[index] is 0:
                roots.append(index)
        return roots

    '''Function: public boolean validate_vertex
       Parameters: int vertex
       Description: checks if a vertex is available in the range 
                    of the digraph. True if vertex is integer 
                    type and available, otherwise False
       returns: boolean True or False'''
    def validate_vertex(self, v):
        return (type(v) is int) and (v >= 0) and (v < self.V)

    '''Function: public boolean check_cyclic
       Parameters: --
       Description: checks if there is a cycle in a digraph. 
                    This can be done by iteratively going 
                    through every vertex and search for a path 
                    that eventually reaches the current vertex 
                    itself. This makes sure that the digraph 
                    is a acyclic to perform compute LCA 
       returns: boolean True/False'''
    def check_cyclic(self):
        self.check_vertex()
        visit = [False] * self.V
        remarked = [False] * self.V
        for v in range(self.V):
            if visit[v] is False:
                if self.__check_cyclic(v, visit, remarked):
                    return True
        return False

    '''Function: private boolean __check_cyclic
       Parameters: int vertex, boolean [] visit, boolean []remarked
       Description: recursively goes through every vertex 
                    in the digraph, marking them every time
                    a vertex is passed through and if the 
                    marked vertex is transversed again, the 
                    digraph has a cycle.
       returns: boolean True/False'''
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

    '''Function: public int get_vertex
       Parameters: --
       Description: returns number of vertices in the digraph
       returns: int V'''
    def get_vertex(self):
        return self.V

    '''Function: public int get_edge
       Parameters: --
       Description: returns number of edges in the digraph
       returns: int E'''
    def get_edge(self):
        return self.E

    '''Function: public void bfs
       Parameters: int source
       Description: performs breadth first search to compute all 
                   the vertices accessible to the root. Utilise 
                   a FIFO queue to store all vertices incident 
                   to current vertex and iterate through them, mark
                   any vertex that has been transvered before.
       returns: --'''
    def bfs(self, s):
        self.marked = [False] * self.V
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

    '''Function: public boolean haspathto
       Parameters: int vertex
       Description: checks if there exist a path between a vertex
                    and the root.
       returns: boolean marked[v]'''
    def haspathto(self, v):
        self.validate_vertex(v)
        return self.marked[v]

    '''Function: public int [] compute_lca2
       Parameters: int root, int vertex, int vertex2
       Description: computes the Lowest Common Ancestor by finding 
                    all paths from both vertices to the root, arranging 
                    arranging them in a depth level default dict, 
                    then intersect the arranged list in the dict in 
                    increasing order of the depth. This way, all the 
                    lowest common ancestor can be found. Returns -1 if 
                    root,vertex and vertex2 are validated False, -2 if 
                    graph not acyclic and -3 if no path from root to 
                    either one of the vertex parameters.
       returns: int [] lca'''
    def compute_lca2(self, root, v, w):
        if not (self.validate_vertex(root) and self.validate_vertex(v) and self.validate_vertex(w)):
            return -1
        elif self.check_cyclic():
            return -2
        self.bfs(root)
        self.check_vertex()

        if self.haspathto(v) and self.haspathto(w):
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

        else:
            return -3

    '''Function: public int [] find_all_paths
       Parameters: int root, int vertex
       Description: finds all paths from 'root' to 'vertex' and store 
                    them in a walk list
       returns: int [] walk'''
    def find_all_paths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * self.V
        walk = list()

        # Create an array to store paths
        path = []

        # Call the recursive helper function to find all paths
        self.__find_all_paths_util(s, d, visited, path, walk)
        return walk

    '''Function: private void __find_all_paths
       Parameters: int current vertex, int vertex, boolean [] visited, 
                   Queue path, int [] walk
       Description: A recursive function to find all paths from 'u' to 'd'. 
                    visited[] keeps track of vertices in current path. 
                    path[] stores actual vertices and path_index is current 
                    index in path[]. Stores the path in the walk list every
                    time the destination vertex is reached, otherwise pop the 
                    path out 
       returns: --'''
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

    '''Function: public int [] arrangedepth
       Parameters: int [] walk, int vertex
       Description: arrange the walk acquired from find all paths in 
                    depth order and store them in a defaultdict for 
                    easier comparism in terms of intersection. 
       returns: defaultdict newwalk'''
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

    '''Function: public static list intersect
       Parameters: list a, list b
       Description: intersect two list to get the common vertices 
       returns: list (a&b)'''
    @staticmethod
    def intersect(a, b):
        return list(set(a) & set(b))

    '''Function: public defaultdict print_digraph
       Parameters: --
       Description: returns the digraph
       returns: defaultdict digraph'''
    def print_digraph(self):
        return self.digraph
