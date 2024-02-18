class Graph:
    def __init__(self, name, num_vertex):
        self.name = name
        self.num_vertex = num_vertex
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])