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

#TODO
Find root, check incidence
Check Acyclic
Find LCA
