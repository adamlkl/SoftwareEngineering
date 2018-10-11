from collections import defaultdict


class Digraph:

    def __init__(self, vertices, edges):
        self.V = int(vertices)
        self.E = int(edges)
        self.digraph = defaultdict(list)
        self.indegree = [0] * self.V

    def add_vertex(self, v, adj):
        if self.validate_vertex(v) and self.validate_vertex(adj):
            self.digraph[v].append(adj)
            self.indegree[adj] += 1

    def get_vertex(self):
        return self.V

    def get_edge(self):
        return self.E

    def validate_vertex(self, v):
        return (type(v) is int) and (v >= 0) and (v < self.V)

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

#TODO
Find root, check incidence
Check Acyclic
Find LCA
