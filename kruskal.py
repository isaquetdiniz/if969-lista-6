from graph import Graph


def kruskal(graph: Graph):
    result = []
    i, e = 0, 0

    sorted_graph = sorted(graph.graph, key=lambda item: item[2])

    parent = []
    rank = []

    for node in range(graph.num_vertex):
        parent.append(node)
        rank.append(0)


    while e < graph.num_vertex - 1 and i < len(sorted_graph):
        u, v, w = sorted_graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e = e + 1
            result.append([u, v, w])
            apply_union(parent, rank, x, y)

    new_graph = Graph('minimum_graph', len(result))

    for u, v, weight in result:
        new_graph.add_edge(u, v, weight)

    return new_graph

def find(parent, i):
    if parent[i] == i:
        return i

    return find(parent, parent[i])

def apply_union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1
