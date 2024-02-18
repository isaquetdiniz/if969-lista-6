class Graph:
    def __init__(self, name):
        self.name = name
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def get_num_vertices(self):
        return len(self.graph)