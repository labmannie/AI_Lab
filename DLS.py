graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dls(graph, current_node, goal, depth_limit, current_depth=0):
    print(f"  Visiting: {current_node}  (depth {current_depth})")

    if current_node == goal:
        return True

    if current_depth >= depth_limit:
        return False

    for neighbor in graph[current_node]:
        if dls(graph, neighbor, goal, depth_limit, current_depth + 1):
            return True

    return False

start = 'A'
goal = 'F'
limit = 2

print(f"DLS: Searching for '{goal}' from '{start}' with depth limit = {limit}\n")

if dls(graph, start, goal, limit):
    print("\nGoal found!")
else:
    print("\nGoal not found within depth limit.")
