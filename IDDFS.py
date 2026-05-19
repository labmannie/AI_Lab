graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dls(graph, current_node, goal, depth_limit, current_depth=0):
    print(f"    Visiting: {current_node}  (depth {current_depth})")

    if current_node == goal:
        return True

    if current_depth >= depth_limit:
        return False

    for neighbor in graph[current_node]:
        if dls(graph, neighbor, goal, depth_limit, current_depth + 1):
            return True

    return False


def iddfs(graph, start, goal, max_depth=10):
    for depth_limit in range(max_depth + 1):
        print(f"\n  --- Trying depth limit = {depth_limit} ---")

        if dls(graph, start, goal, depth_limit):
            print(f"\n  Goal '{goal}' found at depth limit = {depth_limit}!")
            return True

    print(f"\nGoal '{goal}' not found within max depth = {max_depth}.")
    return False


start = 'A'
goal  = 'F'

print(f"IDDFS: Searching for '{goal}' from '{start}'\n")
iddfs(graph, start, goal)
