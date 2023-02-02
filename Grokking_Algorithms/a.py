from collections import deque, defaultdict

from graph_graph import show_graph, to_adjacency_list

# Chapter 6 Unweighted Graph
graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


# show_graph(graph)


def person_is_seller(name: str) -> bool:
    mango_sellers = ['alice', 'anuj']
    return name in mango_sellers


def search_seller(graph: dict, src: str) -> str:
    visited = {src}
    q = deque([src])

    sellers = []
    while q:
        crt = q.popleft()
        if person_is_seller(crt):
            sellers.append(crt)
        for neighbor in graph[crt]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

    return sellers


print(search_seller(graph, 'you'))


# Unweighted graph
def shortest_distance(graph, src, dst):
    visited = {src}
    q = deque([(src, 0)])

    while q:
        crt, distance = q.popleft()
        if crt == dst:
            return distance
        for neighbor in graph[crt]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, distance + 1))
    return -1


print(shortest_distance(graph, 'you', 'anuj'))


# graph = {
#     'a': ['c', 'b'],
#     'c': ['a', 'b', 'd'],
#     'b': ['a', 'c', 'd'],
#     'd': ['c', 'b', 'e'],
#     'e': ['d'],
#     'g': ['f'],
#     'f': ['g']
# }
# print(graph)
# show_graph(graph)
# print(shortest_distance(graph, 'a', 'e'))


# Chapter 7 Dijkstra's Algorithm (Wighted Graph): It only works for directed acyclic graphs(DAGs)


# graph = defaultdict(dict)
# graph["start"]["a"] = 6
# graph["start"]["b"] = 2
# graph['a']['finish'] = 1
# graph['b']['finish'] = 5
# graph['b']['a'] = 3


def dijkstra(graph, src, dst):
    # initialize the costs table
    costs = {k: v for k, v in graph[src].items()}
    for k in graph:
        if k not in costs and k is not src:
            costs[k] = float('inf')
    print('costs table: ', costs)

    # initialize the parents table
    parents = {k: src for k in graph[src].keys()}
    # for k in graph:
    #     if k not in parents and k is not src:
    #         parents[k] = None
    print('parents table: ', parents)
    processed = set()

    def find_lowest_cost_node(costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    # Find the lowest-cost node that you haven't processed yet.
    node = find_lowest_cost_node(costs)
    # print(node)
    # If you've processed all the nodes, this while loop is done.
    while node is not None:
        cost = costs[node]
        # Go through all the neighbors of this node.
        neighbors = graph[node]
        for n in neighbors.keys():
            # print(n)
            new_cost = cost + neighbors[n]
            # print(n, new_cost)
            # If it's cheaper to get to this neighbor by going through this node...
            if costs[n] > new_cost:
                # ... update the cost for this node.
                costs[n] = new_cost
                # This node becomes the new parent for this neighbor.
                parents[n] = node
            # print('costs: ', costs)
            # print('parents:', parents)
        # Mark the node as processed.
        processed.add(node)
        node = find_lowest_cost_node(costs)
    return costs, costs[dst]


graph = {
    'start': {
        'a': 6,
        'b': 2
    },
    'a': {
        'fin': 1
    },
    'b': {
        'fin': 5,
        'a': 3
    },
    'fin': {}
}


graph = {
    'start': {
        'a': 5,
        'c': 2
    },
    'a': {
        'b': 4,
        'd': 2
    },
    'b': {
        'fin': 3,
        'd': 6
    },
    'c': {
        'a': 8,
        'd': 7
    },
    'd': {
        'fin': 1
    },
    'fin': {}
}

# graph = {
#     'start': {
#         'a': 10,
#     },
#     'a': {
#         'b': 20
#     },
#     'b': {
#         'fin': 30,
#         'c': 1
#     },
#     'c': {
#         'a': 1
#     },
#     'fin': {}
# }

graph = {
    'book': {
        'lp': 5,
        'poster': 0
    },
    'lp': {
        'guitar': 15,
        'drums': 20
    },
    'poster': {
        'drums': 35,
        'guitar': 30
    },
    'drums': {
        'piano': 10
    },
    'guitar': {
        'piano': 20
    },
    'piano': {}

}

print('graph table: ', graph)

# print(dijkstra(graph, 'start', 'fin'))
print(dijkstra(graph, 'book', 'piano'))