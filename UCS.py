# Program 6: Uniform Cost Search (UCS) Algorithm
# Finds the least-cost path from a start node to a goal node using a Priority Queue

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        """Add item with given priority to the queue."""
        self.queue.append((priority, item))
        # Sort by priority (ascending) after each insertion
        self.queue.sort(key=lambda x: x[0])

    def dequeue(self):
        """Remove and return the item with the lowest priority (cost)."""
        if not self.is_empty():
            return self.queue.pop(0)  # Returns (priority, item)
        return None

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.queue) == 0


def uniform_cost_search(graph, start, goal):
    """
    Perform Uniform Cost Search to find the least-cost path.

    Args:
        graph: dict of {node: [(neighbor, cost), ...]}
        start: starting node
        goal:  goal node

    Returns:
        (total_cost, path) tuple
    """
    # Priority queue stores (cost, path)
    pq = PriorityQueue()
    pq.enqueue([start], 0)

    # Track visited nodes
    visited = set()

    while not pq.is_empty():
        cost, path = pq.dequeue()
        current_node = path[-1]

        # Goal check
        if current_node == goal:
            return (cost, path)

        # Skip already visited nodes
        if current_node in visited:
            continue
        visited.add(current_node)

        # Expand neighbors
        for neighbor, edge_cost in graph.get(current_node, []):
            if neighbor not in visited:
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                pq.enqueue(new_path, new_cost)

    return (float('inf'), [])  # No path found


# ── Graph Definition ──────────────────────────────────────────────────────────
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# ── Run UCS ───────────────────────────────────────────────────────────────────
result = uniform_cost_search(graph, 'A', 'G')
print("Cost and Path:", result)
