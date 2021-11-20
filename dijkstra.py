def format_path(path):
    return str(path).replace('[', '').replace(']', '').replace("'", '').replace(', ', ' -> ')


def dijkstra(graph, start, goal):
    distance_cost = {}  # records the cost to reach an optimal node
    path_taken = {}  # keep track of the path that has led us to this node
    unseen_nodes = graph  # all paths start as unseen
    infinity = 99999  # basically the worst cost among the options
    track_optimal_path = []  # this variable will store the path taken

    for node in unseen_nodes:
        distance_cost[node] = infinity

    distance_cost[start] = 0

    while unseen_nodes:
        current_node = None

        for node in unseen_nodes:
            if current_node is None:
                current_node = node
            elif distance_cost[node] < distance_cost[current_node]:
                current_node = node

        path_options = graph[current_node].items()

        for child_node, weight in path_options:
            if distance_cost[current_node] + weight < distance_cost[child_node]:
                distance_cost[child_node] = distance_cost[current_node] + weight
                path_taken[child_node] = current_node

        unseen_nodes.pop(current_node)

    current_node = goal

    while current_node != start:
        try:
            track_optimal_path.insert(0, current_node)
            current_node = path_taken[current_node]
        except KeyError:
            print("Path is not reachable")
            break

    track_optimal_path.insert(0, start)

    if distance_cost[goal] != infinity:
        print("Shortest distance value is of:", str(distance_cost[goal]))
        print("Optimal path is:", format_path(track_optimal_path))


if __name__ == '__main__':
    cities_graph = {
        'Philadelphia': {'Pittsburg': 320},
        'Pittsburg': {'Cleveland': 130, 'Columbus': 180},
        'Cleveland': {'Toledo': 120, 'Columbus': 150},
        'Columbus': {'Indianapolis': 180, 'Toledo': 155},
        'Toledo': {'Detroit': 60, 'Ann Arbor': 40},
        'Detroit': {'Ann Arbor': 50},
        'Ann Arbor': {'Chicago': 260},
        'Chicago': {'Fort Wayne': 148, 'Indianapolis': 180},
        'Indianapolis': {'Fort Wayne': 120, 'Chicago': 180},
        'Fort Wayne': {'Indianapolis': 120, 'Chicago': 148}
    }

    dijkstra(cities_graph, 'Philadelphia', 'Fort Wayne')
