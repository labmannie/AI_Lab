# Program 7: 8-Puzzle Problem using A* Search Algorithm
# Heuristic: Manhattan Distance

import heapq

# ── Board Class ───────────────────────────────────────────────────────────────

class PuzzleBoard:
    GOAL_STATE = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]

    def __init__(self, state, parent=None, move="", g=0):
        self.state  = state          # 3x3 list
        self.parent = parent         # parent PuzzleBoard
        self.move   = move           # move description that led here
        self.g      = g              # cost from start (depth)
        self.h      = self.manhattan_distance()
        self.f      = self.g + self.h

    # ── Display ───────────────────────────────────────────────────────────────

    def display(self):
        for row in self.state:
            print(" ".join(str(x) if x != 0 else "_" for x in row))
        print()

    # ── Goal check ────────────────────────────────────────────────────────────

    def is_goal(self):
        return self.state == self.GOAL_STATE

    # ── Heuristic: Manhattan Distance ─────────────────────────────────────────

    def manhattan_distance(self):
        distance = 0
        for r in range(3):
            for c in range(3):
                val = self.state[r][c]
                if val != 0:
                    goal_r, goal_c = divmod(val - 1, 3)
                    distance += abs(r - goal_r) + abs(c - goal_c)
        return distance

    # ── Find blank (0) tile ───────────────────────────────────────────────────

    def find_blank(self):
        for r in range(3):
            for c in range(3):
                if self.state[r][c] == 0:
                    return r, c

    # ── Generate successors ───────────────────────────────────────────────────

    def get_successors(self):
        successors = []
        r, c = self.find_blank()

        # (direction_name, row_delta, col_delta, tile_moves_in_this_direction)
        moves = [
            ("up",    -1,  0),   # blank moves up    → tile below moves up
            ("down",   1,  0),   # blank moves down  → tile above moves down
            ("left",   0, -1),   # blank moves left  → tile right moves left
            ("right",  0,  1),   # blank moves right → tile left moves right
        ]

        for direction, dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = [row[:] for row in self.state]   # deep copy
                # swap blank with the adjacent tile
                tile = new_state[nr][nc]
                new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]

                move_desc = f"Move {tile} {direction}"
                successors.append(
                    PuzzleBoard(new_state, parent=self, move=move_desc, g=self.g + 1)
                )

        return successors

    # ── Comparison for heapq (min-heap on f) ─────────────────────────────────

    def __lt__(self, other):
        return self.f < other.f

    # ── Hashable state for visited set ────────────────────────────────────────

    def state_tuple(self):
        return tuple(tuple(row) for row in self.state)


# ── A* Search ────────────────────────────────────────────────────────────────

def astar(initial_state):
    start = PuzzleBoard(initial_state)

    open_heap = []
    heapq.heappush(open_heap, start)

    visited = {}   # state_tuple -> best g seen

    while open_heap:
        current = heapq.heappop(open_heap)

        if current.is_goal():
            return current                          # goal reached

        key = current.state_tuple()
        if key in visited and visited[key] <= current.g:
            continue                                # skip worse path
        visited[key] = current.g

        for successor in current.get_successors():
            s_key = successor.state_tuple()
            if s_key not in visited or visited[s_key] > successor.g:
                heapq.heappush(open_heap, successor)

    return None                                     # no solution


# ── Reconstruct path ─────────────────────────────────────────────────────────

def reconstruct_path(goal_node):
    path = []
    node = goal_node
    while node:
        path.append(node)
        node = node.parent
    path.reverse()
    return path


# ── Print solution ────────────────────────────────────────────────────────────

def print_solution(path):
    print("=" * 35)
    print("       8-PUZZLE  A* SOLUTION")
    print("=" * 35)
    print("\nInitial State:")
    path[0].display()

    for step, node in enumerate(path[1:], start=1):
        print(f"Step {step}: {node.move}")
        node.display()

    print("=" * 35)
    print(f"  Goal reached in {len(path) - 1} moves!")
    print("=" * 35)
    print("\nMove Sequence:")
    for step, node in enumerate(path[1:], start=1):
        print(f"  Move {step}: {node.move}")


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    print("\nSolving 8-Puzzle using A* (Manhattan Distance heuristic)...\n")

    goal_node = astar(initial_state)

    if goal_node:
        path = reconstruct_path(goal_node)
        print_solution(path)
    else:
        print("No solution exists for this puzzle configuration.")
