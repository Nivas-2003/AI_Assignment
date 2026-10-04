import heapq

# ---------------------------------------------------
# Q1: Dijkstra / Uniform Cost Search
# Indian Cities Road Network
# ---------------------------------------------------

graph = {

    "Delhi": {
        "Jaipur": 280,
        "Lucknow": 550,
        "Chandigarh": 245,
        "Agra": 230
    },

    "Jaipur": {
        "Delhi": 280,
        "Ahmedabad": 670,
        "Agra": 240,
        "Udaipur": 395
    },

    "Lucknow": {
        "Delhi": 550,
        "Kanpur": 90,
        "Varanasi": 320,
        "Patna": 530
    },

    "Chandigarh": {
        "Delhi": 245,
        "Amritsar": 230,
        "Shimla": 115
    },

    "Agra": {
        "Delhi": 230,
        "Jaipur": 240,
        "Kanpur": 290
    },

    "Ahmedabad": {
        "Jaipur": 670,
        "Mumbai": 530,
        "Vadodara": 110
    },

    "Udaipur": {
        "Jaipur": 395,
        "Ahmedabad": 260
    },

    "Kanpur": {
        "Lucknow": 90,
        "Agra": 290,
        "Prayagraj": 200
    },

    "Varanasi": {
        "Lucknow": 320,
        "Patna": 250,
        "Prayagraj": 125
    },

    "Patna": {
        "Lucknow": 530,
        "Varanasi": 250,
        "Kolkata": 580
    },

    "Prayagraj": {
        "Kanpur": 200,
        "Varanasi": 125
    },

    "Mumbai": {
        "Ahmedabad": 530,
        "Pune": 150,
        "Nashik": 170
    },

    "Vadodara": {
        "Ahmedabad": 110,
        "Mumbai": 420
    },

    "Pune": {
        "Mumbai": 150,
        "Nashik": 210,
        "Hyderabad": 560,
        "Bengaluru": 840
    },

    "Nashik": {
        "Mumbai": 170,
        "Pune": 210
    },

    "Hyderabad": {
        "Pune": 560,
        "Bengaluru": 570,
        "Chennai": 630,
        "Nagpur": 500,
        "Visakhapatnam": 620
    },

    "Bengaluru": {
        "Pune": 840,
        "Hyderabad": 570,
        "Chennai": 350,
        "Mysuru": 145
    },

    "Chennai": {
        "Hyderabad": 630,
        "Bengaluru": 350
    },

    "Mysuru": {
        "Bengaluru": 145
    },

    "Nagpur": {
        "Hyderabad": 500,
        "Bhopal": 350
    },

    "Bhopal": {
        "Nagpur": 350,
        "Indore": 190
    },

    "Indore": {
        "Bhopal": 190,
        "Mumbai": 580
    },

    "Amritsar": {
        "Chandigarh": 230
    },

    "Shimla": {
        "Chandigarh": 115
    },

    "Kolkata": {
        "Patna": 580,
        "Bhubaneswar": 440
    },

    "Bhubaneswar": {
        "Kolkata": 440,
        "Visakhapatnam": 440
    },

    "Visakhapatnam": {
        "Bhubaneswar": 440,
        "Hyderabad": 620
    }
}


# ---------------------------------------------------
# Dijkstra's Algorithm
# ---------------------------------------------------

def dijkstra(graph, start, goal):

    # Initially, distance to every city is infinity
    distances = {}

    # Store previous city for path reconstruction
    previous = {}

    # Store visited cities
    visited = set()

    for city in graph:
        distances[city] = float("inf")
        previous[city] = None

    distances[start] = 0

    # Priority queue
    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_city = heapq.heappop(priority_queue)

        # Skip if city was already visited
        if current_city in visited:
            continue

        visited.add(current_city)

        # Goal reached
        if current_city == goal:
            break

        # Check neighboring cities
        for neighbor, road_distance in graph[current_city].items():

            new_distance = current_distance + road_distance

            # Found a shorter path
            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current_city

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    # No route found
    if distances[goal] == float("inf"):
        return None, None, visited

    # ------------------------------------------------
    # Reconstruct shortest path
    # ------------------------------------------------

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path, distances[goal], visited


# ---------------------------------------------------
# Display available cities
# ---------------------------------------------------

print("\n==============================================")
print("   DIJKSTRA / UNIFORM COST SEARCH")
print("   INDIAN CITY ROAD NETWORK")
print("==============================================")

print("\nAvailable Cities:")

for city in sorted(graph):
    print("-", city)


# ---------------------------------------------------
# User Input
# ---------------------------------------------------

start = input("\nEnter starting city: ").strip()
goal = input("Enter destination city: ").strip()


# ---------------------------------------------------
# Validate Input
# ---------------------------------------------------

if start not in graph:

    print("\nInvalid starting city.")
    print("Please enter a city from the available list.")

elif goal not in graph:

    print("\nInvalid destination city.")
    print("Please enter a city from the available list.")

else:

    # Run Dijkstra
    path, distance, visited = dijkstra(graph, start, goal)

    # ------------------------------------------------
    # Display Result
    # ------------------------------------------------

    if path is None:

        print("\nNo route found between the selected cities.")

    else:

        print("\n==============================================")
        print("              SEARCH RESULT")
        print("==============================================")

        print("\nStarting City :", start)
        print("Destination   :", goal)

        print("\nShortest Route:")

        print(" -> ".join(path))

        print("\nTotal Road Distance:", distance, "km")

        print("Number of Cities Explored:", len(visited))

        print("\nCities Explored:")

        for city in sorted(visited):
            print("-", city)

        print("\n==============================================")
        print("Dijkstra Search Completed Successfully")
        print("==============================================")