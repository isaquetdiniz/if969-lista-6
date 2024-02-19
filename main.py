import csv

from graph import Graph
from kruskal import kruskal
from networkx_graph import print_graph

edges = []
max_lines = 100
max_number = 0

with open('input/soc-sign-bitcoinotc.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')

    for row in spamreader:
        if spamreader.line_num > max_lines:
           break

        source = int(row[0])
        target = int(row[1])
        rating = int(row[2])

        max_number = max(source, target, max_number)

        source -= 1
        target -= 1

        edges.append([source, target, rating])

graph = Graph('initial_graph', max_number)

for source, target, rating in edges:
    graph.add_edge(source, target, rating)

minimum_graph = kruskal(graph)

print_graph(graph)
print_graph(minimum_graph)