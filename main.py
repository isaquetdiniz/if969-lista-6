import csv

from graph import Graph
from kruskal import kruskal
from networkx_graph import print_graph

with open('input/postes_recife.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',')

    for row in spamreader:
        print(row['\ufeff_id'], row['ID PONTO'], row['LATITUDE'], row['LONGITUDE'])

graph = Graph('initial_graph')

graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 2)
graph.add_edge(1, 0, 4)
graph.add_edge(2, 0, 4)
graph.add_edge(2, 1, 2)
graph.add_edge(2, 3, 3)
graph.add_edge(2, 5, 2)
graph.add_edge(2, 4, 4)
graph.add_edge(3, 2, 3)
graph.add_edge(3, 4, 3)
graph.add_edge(4, 2, 4)
graph.add_edge(4, 3, 3)
graph.add_edge(5, 2, 2)
graph.add_edge(5, 4, 3)

minimum_graph = kruskal(graph)

print_graph(graph)
print_graph(minimum_graph)