from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    print("BFS Traversal Order:")
    while queue:
        current_node = queue.popleft()

        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)

bfs(graph, 'A')
