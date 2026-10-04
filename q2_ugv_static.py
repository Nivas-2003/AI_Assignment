import random
import heapq
import time

# Battlefield size
ROWS = 70
COLS = 70


# -------------------------------------------------
# Heuristic: Manhattan Distance
# -------------------------------------------------
def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


# -------------------------------------------------
# Generate random battlefield
# -------------------------------------------------
def generate_grid(density):

    grid = []

    for i in range(ROWS):

        row = []

        for j in range(COLS):

            if random.random() < density:
                row.append(1)       # Obstacle
            else:
                row.append(0)       # Free space

        grid.append(row)

    return grid


# -------------------------------------------------
# A* Search Algorithm
# -------------------------------------------------
def a_star(grid, start, goal):

    # Priority queue
    open_list = []

    heapq.heappush(open_list, (0, start))

    # Cost from start
    g_cost = {start: 0}

    # Parent of each node
    parent = {start: None}

    # Explored nodes
    visited = set()

    while open_list:

        f_cost, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        # Goal reached
        if current == goal:

            path = []

            node = goal

            while node is not None:

                path.append(node)
                node = parent[node]

            path.reverse()

            return path, visited

        row, col = current

        # Four possible movements
        neighbors = [
            (row - 1, col),       # Up
            (row + 1, col),       # Down
            (row, col - 1),       # Left
            (row, col + 1)        # Right
        ]

        for nr, nc in neighbors:

            # Outside grid
            if nr < 0 or nr >= ROWS:
                continue

            if nc < 0 or nc >= COLS:
                continue

            # Obstacle
            if grid[nr][nc] == 1:
                continue

            neighbor = (nr, nc)

            new_cost = g_cost[current] + 1

            # Better path found
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:

                g_cost[neighbor] = new_cost

                h_cost = heuristic(
                    neighbor,
                    goal
                )

                f_cost = new_cost + h_cost

                parent[neighbor] = current

                heapq.heappush(
                    open_list,
                    (f_cost, neighbor)
                )

    # No path found
    return None, visited


# -------------------------------------------------
# Display battlefield
# -------------------------------------------------
def display_grid(grid, path, start, goal):

    path_set = set(path)

    for i in range(ROWS):

        line = ""

        for j in range(COLS):

            position = (i, j)

            if position == start:
                line += "S "

            elif position == goal:
                line += "G "

            elif position in path_set:
                line += "* "

            elif grid[i][j] == 1:
                line += "# "

            else:
                line += ". "

        print(line)


# -------------------------------------------------
# Run one experiment
# -------------------------------------------------
def run_experiment(name, density):

    print("\n")
    print("==============================================")
    print(name, "OBSTACLE DENSITY")
    print("==============================================")

    start = (0, 0)
    goal = (ROWS - 1, COLS - 1)

    # Generate grid until a path exists
    while True:

        grid = generate_grid(density)

        # Start and goal must be free
        grid[start[0]][start[1]] = 0
        grid[goal[0]][goal[1]] = 0

        path, visited = a_star(
            grid,
            start,
            goal
        )

        if path is not None:
            break

    # Measure execution time
    start_time = time.perf_counter()

    path, visited = a_star(
        grid,
        start,
        goal
    )

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Count obstacles
    obstacle_count = 0

    for row in grid:
        obstacle_count += row.count(1)

    print("\nStart Position :", start)
    print("Goal Position  :", goal)

    print("Grid Size      :", ROWS, "x", COLS)

    print("Obstacle Count :", obstacle_count)

    print("Obstacle Density:", density * 100, "%")

    print("Cells Explored :", len(visited))

    if path is not None:

        path_length = len(path) - 1

        print("Path Length    :", path_length)

        print(
            "Execution Time :",
            round(execution_time, 6),
            "seconds"
        )

        print("Mission Status : SUCCESS")

        print("\nPath Coordinates:")

        print(path)

        print("\nBattlefield Map:")

        display_grid(
            grid,
            path,
            start,
            goal
        )

    else:

        print("Path Length    : Not Found")

        print(
            "Execution Time :",
            round(execution_time, 6),
            "seconds"
        )

        print("Mission Status : FAILED")


# -------------------------------------------------
# Main Program
# -------------------------------------------------

print("==============================================")
print("      UGV STATIC OBSTACLE NAVIGATION")
print("==============================================")

print("\nBattlefield: 70 x 70 km")

print("\nThe UGV uses A* search to find")
print("the shortest path while avoiding obstacles.")

# Low density
run_experiment(
    "LOW",
    0.10
)

# Medium density
run_experiment(
    "MEDIUM",
    0.25
)

# High density
run_experiment(
    "HIGH",
    0.40
)