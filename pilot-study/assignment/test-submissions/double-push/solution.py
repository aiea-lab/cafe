import graph

def BFS(initial_node, goal_node, frontier):
    if initial_node == goal_node:
        return []

    frontier.push((list([initial_node.label]), initial_node))

    while (not frontier.is_empty()):
        (path, node) = frontier.pop()
        for neighbor in node.neighbors:
            neighbor_path = path + [neighbor.label]
            if (neighbor == goal_node):
                return neighbor_path
            frontier.push((path, node))
            frontier.push((neighbor_path, neighbor))

    raise ValueError("No solution Found.")
