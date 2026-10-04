import random
import heapq
import time

ROWS = 30
COLS = 30


# ---------------------------------------------
# Manhattan Distance
# ---------------------------------------------
def heuristic(current, goal):

    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


# ---------------------------------------------
# Create initial battlefield
# ---------------------------------------------
def create_grid():

    grid = []

    for i in range(ROWS):

        row = []

        for j in range(COLS):

            if random.random() < 0.15:
                row.append(1)
            else:
                row.append(0)

        grid.append(row)

    return grid


# ---------------------------------------------
# A* Search
# ---------------------------------------------
def a_star(grid, start, goal):

    open_list = []

    heapq.heappush(
        open_list,
        (0, start)
    )

    g_cost = {
        start: 0
    }

    parent = {
        start: None
    }

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

        neighbors = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
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

    return None, visited


# ---------------------------------------------
# Display the battlefield
# ---------------------------------------------
def display_grid(grid, current, goal):

    for i in range(ROWS):

        line = ""

        for j in range(COLS):

            position = (i, j)

            if position == current:

                line += "U "

            elif position == goal:

                line += "G "

            elif grid[i][j] == 1:

                line += "# "

            else:

                line += ". "

        print(line)


# ---------------------------------------------
# Add a dynamic obstacle
# ---------------------------------------------
def add_dynamic_obstacle(grid, current, goal):

    # Try several times to find a valid location

    for _ in range(100):

        row = random.randint(0, ROWS - 1)
        col = random.randint(0, COLS - 1)

        obstacle = (row, col)

        # Do not put obstacle on UGV or goal
        if obstacle == current:
            continue

        if obstacle == goal:
            continue

        # Only add if currently free
        if grid[row][col] == 0:

            grid[row][col] = 1

            return obstacle

    return None


# ---------------------------------------------
# Dynamic UGV Navigation
# ---------------------------------------------
def dynamic_ugv():

    grid = create_grid()

    start = (0, 0)
    goal = (ROWS - 1, COLS - 1)

    # Start and goal must be free
    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0

    current = start

    total_steps = 0
    replanning_count = 0
    dynamic_obstacles = 0
    total_cells_explored = 0

    start_time = time.perf_counter()

    print("\nInitial path calculation...")

    path, visited = a_star(
        grid,
        current,
        goal
    )

    if path is None:

        print("No initial path exists.")
        return

    total_cells_explored += len(visited)

    print("Initial path found.")
    print("Initial path length:", len(path) - 1)

    # -----------------------------------------
    # Main movement loop
    # -----------------------------------------

    while current != goal:

        # If there is no path, calculate one
        if path is None or len(path) < 2:

            path, visited = a_star(
                grid,
                current,
                goal
            )

            total_cells_explored += len(visited)

            replanning_count += 1

            if path is None:

                print("\nNo path available.")
                print("UGV stopped.")

                break

        # -------------------------------------
        # Sometimes a new obstacle appears
        # -------------------------------------

        if random.random() < 0.30:

            obstacle = add_dynamic_obstacle(
                grid,
                current,
                goal
            )

            if obstacle is not None:

                dynamic_obstacles += 1

                print(
                    "\nDynamic obstacle detected at:",
                    obstacle
                )

        # -------------------------------------
        # Look at next position
        # -------------------------------------

        next_position = path[1]

        # -------------------------------------
        # If new obstacle blocks the path
        # -------------------------------------

        if grid[
            next_position[0]
        ][
            next_position[1]
        ] == 1:

            print(
                "Current path blocked at:",
                next_position
            )

            print("Replanning...")

            path, visited = a_star(
                grid,
                current,
                goal
            )

            total_cells_explored += len(visited)

            replanning_count += 1

            if path is None:

                print("No alternative path found.")

                break

            continue

        # -------------------------------------
        # Move UGV
        # -------------------------------------

        current = next_position

        path = path[1:]

        total_steps += 1

        print(
            "UGV moved to:",
            current
        )

        # Small probability of another obstacle
        # appearing after movement
        if random.random() < 0.20:

            obstacle = add_dynamic_obstacle(
                grid,
                current,
                goal
            )

            if obstacle is not None:

                dynamic_obstacles += 1

                print(
                    "New obstacle appeared at:",
                    obstacle
                )

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # -----------------------------------------
    # Results
    # -----------------------------------------

    print("\n")
    print("==============================================")
    print("       DYNAMIC UGV NAVIGATION RESULTS")
    print("==============================================")

    print("\nStart Position       :", start)

    print("Goal Position        :", goal)

    print("Final Position       :", current)

    print("Grid Size            :", ROWS, "x", COLS)

    print("Total Steps          :", total_steps)

    print("Dynamic Obstacles    :", dynamic_obstacles)

    print("Number of Replanning :", replanning_count)

    print(
        "Cells Explored       :",
        total_cells_explored
    )

    print(
        "Execution Time       :",
        round(execution_time, 6),
        "seconds"
    )

    if current == goal:

        print("Mission Status       : SUCCESS")

    else:

        print("Mission Status       : FAILED")

    print("\nFinal Battlefield:")

    display_grid(
        grid,
        current,
        goal
    )


# ---------------------------------------------
# Main
# ---------------------------------------------

print("==============================================")
print("       UGV DYNAMIC OBSTACLE NAVIGATION")
print("==============================================")

print("\nGrid Size: 30 x 30")

print("\nThe UGV uses A* and dynamic replanning.")

dynamic_ugv()