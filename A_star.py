from queue import PriorityQueue

def a_star(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    came_from = {start: None}
    cost = {start: 0}

    while not pq.empty():
        _, current = pq.get()

        if current == goal:
            break

        for neighbor, weight in graph[current]:
            new_cost = cost[current] + weight
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost
                pq.put((priority, neighbor))
                came_from[neighbor] = current

    # Reconstruct path
    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from.get(node)
    path.reverse()

    print("Shortest Path using A*:", path)
    print("Total Cost:", cost[goal])

# Example graph (without heuristic for simplicity)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

a_star(graph, 'A', 'F')
