# pip install networkx matplotlib
# https://networkx.org/documentation/stable/tutorial.html
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict, deque


# graph = {
#     'a': ['b', 'c', 'd'],
#     'c': ['d', 'e', 'f']
# }

# graph = {
#     'a': ['b', 'c'],
#     'b': ['d'],
#     'c': ['e'],
#     'd': ['f'],
#     'e': [],
#     'f': []
# }

def to_adjacency_list(edges):
    graph = defaultdict(list)
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    return dict(graph)


def dfs_print(graph, src, visited=set()):
    print(src, end=' ')
    visited.add(src)
    for neighbor in graph[src]:
        if neighbor not in visited:
            dfs_print(graph, neighbor)


def bfs_print(graph, src):
    visited = {src}
    q = deque([src])
    while q:
        current = q.popleft()
        print(current, end=' ')
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)


def show_graph(graph):
    G = nx.Graph()
    if type(graph) == dict:
        for k, v in graph.items():
            if v:
                for i in v:
                    G.add_edge(k, i, weight=1)
            else:
                G.add_node(k)

    elif type(graph) == list:
        # edges = [[0, 1], [1, 2], [2, 0]]
        edges = graph
        for edge in edges:
            G.add_edge(edge[0], edge[1], weight=1)

    # G.add_edge('a', 'b', weight=1)
    # G.add_edge('a', 'c', weight=1)
    # G.add_edge('c', 'd', weight=1)
    # G.add_edge('c', 'e', weight=1)
    # G.add_edge('c', 'f', weight=1)
    # G.add_edge('a', 'd', weight=1)

    # print(G.edges(data=True))

    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]

    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='green')

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge,
                           width=3)
    nx.draw_networkx_edges(G, pos, edgelist=esmall,
                           width=3, alpha=0.2, edge_color='blue', style='dashed')

    # labels
    nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif', font_color='white')

    plt.axis('off')
    plt.show()
