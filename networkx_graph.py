import networkx as nx

from graph import Graph


def print_graph(graph: Graph):
   new_graph = build_graph(graph)

   agraph = nx.nx_agraph.to_agraph(new_graph)
   agraph.layout()
   agraph.layout(prog="dot")
   agraph.draw(f'output/{graph.name}.png', prog="circo")

def build_graph(graph: Graph):
    new_graph = nx.Graph()

    for u, v, weight in graph.graph:
        new_graph.add_edge(u, v, weight=weight)

    return new_graph