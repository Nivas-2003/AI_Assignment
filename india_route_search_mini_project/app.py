from flask import Flask, render_template, request, jsonify
import heapq

app = Flask(__name__)

# Approximate educational road distances in km.
# This is a simplified graph for demonstrating search algorithms,
# not a navigation/routing database.
EDGES = [
    ("Delhi", "Chandigarh", 250),
    ("Delhi", "Jaipur", 280),
    ("Delhi", "Agra", 230),
    ("Delhi", "Lucknow", 550),
    ("Delhi", "Dehradun", 250),
    ("Delhi", "Kanpur", 490),

    ("Chandigarh", "Amritsar", 230),
    ("Chandigarh", "Dehradun", 170),
    ("Chandigarh", "Jaipur", 500),

    ("Amritsar", "Jammu", 210),
    ("Jammu", "Srinagar", 270),

    ("Jaipur", "Agra", 240),
    ("Jaipur", "Ahmedabad", 650),
    ("Jaipur", "Indore", 570),

    ("Agra", "Lucknow", 330),
    ("Agra", "Kanpur", 290),

    ("Lucknow", "Kanpur", 90),
    ("Lucknow", "Varanasi", 320),
    ("Lucknow", "Patna", 540),

    ("Kanpur", "Prayagraj", 200),
    ("Varanasi", "Prayagraj", 120),
    ("Varanasi", "Patna", 250),
    ("Varanasi", "Kolkata", 680),
    ("Prayagraj", "Patna", 330),

    ("Patna", "Ranchi", 330),
    ("Patna", "Kolkata", 580),
    ("Ranchi", "Kolkata", 410),
    ("Ranchi", "Raipur", 570),

    ("Kolkata", "Bhubaneswar", 440),
    ("Kolkata", "Guwahati", 1000),
    ("Bhubaneswar", "Visakhapatnam", 440),
    ("Bhubaneswar", "Raipur", 600),
    ("Visakhapatnam", "Vijayawada", 350),
    ("Vijayawada", "Hyderabad", 275),
    ("Vijayawada", "Chennai", 450),

    ("Hyderabad", "Nagpur", 500),
    ("Hyderabad", "Bengaluru", 570),
    ("Hyderabad", "Pune", 560),
    ("Hyderabad", "Aurangabad", 620),

    ("Nagpur", "Jabalpur", 275),
    ("Nagpur", "Bhopal", 350),
    ("Nagpur", "Raipur", 300),
    ("Nagpur", "Indore", 410),
    ("Jabalpur", "Bhopal", 330),
    ("Jabalpur", "Prayagraj", 370),
    ("Jabalpur", "Raipur", 300),

    ("Bhopal", "Indore", 190),
    ("Indore", "Ahmedabad", 400),
    ("Indore", "Mumbai", 585),

    ("Ahmedabad", "Vadodara", 110),
    ("Ahmedabad", "Surat", 265),
    ("Ahmedabad", "Mumbai", 530),
    ("Vadodara", "Surat", 155),
    ("Surat", "Mumbai", 285),
    ("Surat", "Nashik", 290),

    ("Mumbai", "Pune", 150),
    ("Mumbai", "Nashik", 170),
    ("Nashik", "Aurangabad", 220),
    ("Nashik", "Pune", 210),
    ("Pune", "Aurangabad", 230),
    ("Pune", "Bengaluru", 840),

    ("Bengaluru", "Chennai", 350),
    ("Bengaluru", "Mysuru", 145),
    ("Bengaluru", "Coimbatore", 360),
    ("Bengaluru", "Mangaluru", 350),
    ("Mysuru", "Mangaluru", 250),
    ("Mangaluru", "Kochi", 420),

    ("Chennai", "Coimbatore", 510),
    ("Chennai", "Madurai", 460),
    ("Coimbatore", "Kochi", 190),
    ("Coimbatore", "Madurai", 215),
    ("Madurai", "Kochi", 260),
    ("Madurai", "Thiruvananthapuram", 250),
    ("Kochi", "Thiruvananthapuram", 200),
]

GRAPH = {}
for a, b, d in EDGES:
    GRAPH.setdefault(a, {})[b] = d
    GRAPH.setdefault(b, {})[a] = d

# Fixed schematic positions for the visual network.
POSITIONS = {
    "Srinagar": (8, 8), "Jammu": (14, 15), "Amritsar": (20, 20),
    "Chandigarh": (27, 17), "Dehradun": (33, 12), "Delhi": (36, 23),
    "Jaipur": (30, 35), "Agra": (39, 33), "Lucknow": (48, 35),
    "Kanpur": (45, 43), "Varanasi": (57, 45), "Prayagraj": (51, 52),
    "Patna": (67, 43), "Ranchi": (69, 56), "Kolkata": (83, 45),
    "Guwahati": (94, 25), "Bhubaneswar": (83, 62),
    "Visakhapatnam": (79, 72), "Vijayawada": (69, 78),
    "Hyderabad": (58, 82), "Nagpur": (50, 67), "Jabalpur": (48, 57),
    "Bhopal": (40, 60), "Indore": (34, 65), "Ahmedabad": (20, 60),
    "Vadodara": (23, 69), "Surat": (27, 77), "Mumbai": (25, 88),
    "Nashik": (32, 81), "Aurangabad": (40, 78), "Pune": (39, 88),
    "Raipur": (60, 62), "Bengaluru": (55, 96), "Mysuru": (49, 104),
    "Mangaluru": (42, 103), "Chennai": (68, 100), "Coimbatore": (59, 108),
    "Madurai": (66, 116), "Kochi": (53, 116),
    "Thiruvananthapuram": (58, 126)
}

# Normalize positions to the SVG viewBox.
MIN_Y = min(y for _, y in POSITIONS.values())
MAX_Y = max(y for _, y in POSITIONS.values())
for city, (x, y) in list(POSITIONS.items()):
    POSITIONS[city] = (x, 8 + (y - MIN_Y) * 84 / (MAX_Y - MIN_Y))

def ucs(start, goal):
    queue = [(0, start, [start])]
    best_cost = {start: 0}
    expanded = []
    seen = set()

    while queue:
        cost, city, path = heapq.heappop(queue)

        if cost != best_cost.get(city, float("inf")):
            continue
        if city in seen:
            continue

        seen.add(city)
        expanded.append({"city": city, "cost": cost})

        if city == goal:
            return path, cost, expanded

        for neighbor, distance in GRAPH[city].items():
            new_cost = cost + distance
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor, path + [neighbor]))

    return [], None, expanded

@app.route("/")
def index():
    return render_template(
        "index.html",
        cities=sorted(GRAPH.keys()),
        edges=EDGES,
        positions=POSITIONS
    )

@app.route("/api/search", methods=["POST"])
def search():
    data = request.get_json(silent=True) or {}
    start = data.get("start")
    goal = data.get("goal")

    if start not in GRAPH or goal not in GRAPH:
        return jsonify({"error": "Please select valid cities."}), 400

    if start == goal:
        return jsonify({
            "path": [start],
            "distance": 0,
            "expanded": [{"city": start, "cost": 0}]
        })

    path, distance, expanded = ucs(start, goal)

    if not path:
        return jsonify({"error": "No route exists in the current graph."}), 404

    return jsonify({
        "path": path,
        "distance": distance,
        "expanded": expanded,
        "algorithm": "Uniform Cost Search"
    })

if __name__ == "__main__":
    app.run(debug=True)
