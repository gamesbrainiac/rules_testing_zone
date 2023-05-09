def depth_first_search(graph, node, visited=None):
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(node)
    print(node, end=' ')

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[node]:
        # if neighbor not in visited:
            depth_first_search(graph, neighbor, visited)

    return visited


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
    }

    start_node = 'A'
    print(f"Depth First Search traversal starting from {start_node}:")
    depth_first_search(graph, start_node)
