import time
from A_star_search import astar, graph, weights, heuristic

# Simulation function
def simulate_path(path, visit_order, total_cost):
    print("\nTruck traveling...\n")
    for node in path:
        print(f"Truck is now at: {node}")
        time.sleep(1)

    print("\nDestination reached!")
    print("\nVisited Order:", visit_order)
    print("Optimal Path:", " → ".join(path))
    print("Total Cost:", total_cost)

# Run simulation
if __name__ == "__main__":
    start = "Disaneng"
    goal = "Coligny"

    path, visit_order, total_cost = astar(graph, weights, heuristic, start, goal)
    simulate_path(path, visit_order, total_cost)