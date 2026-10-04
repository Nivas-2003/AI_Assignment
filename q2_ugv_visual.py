import random
import heapq
import time
import matplotlib.pyplot as plt


ROWS = 70
COLS = 70


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def generate_grid(density):

    grid = []

    for i in range(ROWS):

        row = []

        for j in range(COLS):

            if random.random() < density:
                row.append(1)
            else:
                row.append(0)

        grid.append(row)

    return grid


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

        f, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:

            path = []

            node = goal

            while node is not None:

                path.append(node)

                node = parent[node]

            path.reverse()

            return path, visited

        r, c = current

        neighbors = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1)
        ]

        for nr, nc in neighbors:

            if nr < 0 or nr >= ROWS:
                continue

            if nc < 0 or nc >= COLS:
                continue

            if grid[nr][nc] == 1:
                continue

            neighbor = (nr, nc)

            new_cost = g_cost[current] + 1

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:

                g_cost[neighbor] = new_cost

                f_cost = (
                    new_cost
                    + heuristic(neighbor, goal)
                )

                parent[neighbor] = current

                heapq.heappush(
                    open_list,
                    (f_cost, neighbor)
                )

    return None, visited


def show_map(grid, path, start, goal, density):

    plt.figure(figsize=(10, 10))

    # Obstacles
    obstacle_x = []
    obstacle_y = []

    for i in range(ROWS):

        for j in range(COLS):

            if grid[i][j] == 1:

                obstacle_x.append(j)
                obstacle_y.append(i)

    plt.scatter(
        obstacle_x,
        obstacle_y,
        marker="s",
        s=15,
        label="Obstacle"
    )

    # Path
    if path:

        path_x = [p[1] for p in path]
        path_y = [p[0] for p in path]

        plt.plot(
            path_x,
            path_y,
            linewidth=2,
            label="UGV Path"
        )

    # Start
    plt.scatter(
        start[1],
        start[0],
        marker="o",
        s=100,
        label="Start"
    )

    # Goal
    plt.scatter(
        goal[1],
        goal[0],
        marker="X",
        s=120,
        label="Goal"
    )

    plt.title(
        "UGV A* Navigation - "
        + str(int(density * 100))
        + "% Obstacle Density"
    )

    plt.xlabel("X Coordinate")

    plt.ylabel("Y Coordinate")

    plt.gca().invert_yaxis()

    plt.grid(True)

    plt.legend()

    plt.show()


def run():

    print("====================================")
    print("UGV GRAPHICAL SIMULATION")
    print("====================================")

    print("\nSelect obstacle density:")

    print("1. Low - 10%")
    print("2. Medium - 25%")
    print("3. High - 40%")

    choice = input("\nEnter choice: ")

    if choice == "1":
        density = 0.10

    elif choice == "2":
        density = 0.25

    elif choice == "3":
        density = 0.40

    else:
        print("Invalid choice.")
        return

    start = (0, 0)
    goal = (ROWS - 1, COLS - 1)

    while True:

        grid = generate_grid(density)

        grid[start[0]][start[1]] = 0
        grid[goal[0]][goal[1]] = 0

        path, visited = a_star(
            grid,
            start,
            goal
        )

        if path is not None:
            break

    start_time = time.perf_counter()

    path, visited = a_star(
        grid,
        start,
        goal
    )

    end_time = time.perf_counter()

    obstacle_count = sum(
        row.count(1)
        for row in grid
    )

    print("\n========== RESULTS ==========")

    print("Grid Size:", ROWS, "x", COLS)

    print("Obstacle Count:", obstacle_count)

    print(
        "Obstacle Density:",
        density * 100,
        "%"
    )

    print(
        "Cells Explored:",
        len(visited)
    )

    print(
        "Path Length:",
        len(path) - 1
    )

    print(
        "Execution Time:",
        round(
            end_time - start_time,
            6
        ),
        "seconds"
    )

    print("Mission Status: SUCCESS")

    show_map(
        grid,
        path,
        start,
        goal,
        density
    )


run()
