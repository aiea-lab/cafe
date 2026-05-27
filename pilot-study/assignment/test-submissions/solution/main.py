import util

def BFS(initial_node, goal_node):
    frontier = util.Queue()

    if initial_node == goal_node:
        return []

    frontier.enqueue((list([initial_node.label]), initial_node))
    visited = set({initial_node})

    while (not frontier.is_empty()):
        (path, node) = frontier.dequeue()
        for neighbor in node.neighbors:
            neighbor_path = path + [neighbor.label]
            if (neighbor == goal_node):
                return neighbor_path
            if neighbor not in visited:
                visited.add(neighbor)
                frontier.enqueue((neighbor_path, neighbor))

    raise ValueError("No solution Found.")
