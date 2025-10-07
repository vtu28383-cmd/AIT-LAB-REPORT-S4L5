import heapq

graph = {
    'a': [('b', 2), ('d', 4)],
    'b': [('a', 2), ('c', 3)],
    'c': [('b', 3), ('d', 1)],
    'd': [('a', 4), ('c', 1)],
}

heuristic = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path, g_score[goal]

            for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic.get(neighbor, 0)
                heapq.heappush(open_set, (f_score, neighbor))
    return None, float('inf')
path, cost = a_star(graph, 'a', 'd', heuristic)
print("Optimal path:", path)
print("Total cost:", cost)
print("\nNodes in the graph:")
for node in graph.keys():
    print(node)
print("\nCost of every edge in the graph:")
seen_edges = set()
for node in graph:
    for neighbor, weight in graph[node]:
        edge = tuple(sorted((node, neighbor)))
        if edge not in seen_edges:
            print(f"Edge {edge[0]}_{edge[1]}: {weight}")
            seen_edges.add(edge)
