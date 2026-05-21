import graph

def BFS(initial_node, goal_node):
    if initial_node == goal_node:
        return []

    frontier = graph.Queue()
    frontier.push((list([initial_node.label]), initial_node))
    visited = set({initial_node})

    while (not frontier.is_empty()):
        (path, node) = frontier.pop()
        for neighbor in node.neighbors:
            neighbor_path = path + [neighbor.label]
            if (neighbor == goal_node):
                return neighbor_path
            if neighbor not in visited:
                visited.add(neighbor)
                frontier.push((neighbor, neighbor_path))

    raise ValueError("No solution Found.")
