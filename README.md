#  Truck Logistics Route Optimization using A* Search

## Project Description

This project implements the **A* Search algorithm** to determine the optimal route for a delivery truck between different locations.

The algorithm minimizes travel cost by considering:

* Actual distance between locations
* Estimated cost to the destination (heuristic)

---

## How the Algorithm Works

A* uses the formula:

f(n) = g(n) + h(n)

Where:

* **g(n)** = cost from the start node to the current node
* **h(n)** = estimated cost from the current node to the goal
* **f(n)** = total estimated cost

The algorithm selects the node with the lowest **f(n)** value at each step.

---

## Files Included

### 1. A_star_search.py

* Implements the A* algorithm
* Defines the graph, weights, and heuristic values
* Produces the main output:

  * Visited nodes
  * Optimal path
  * Total cost

### 2. A_star_search_testcase.py

* Runs the A* algorithm
* Simulates the truck traveling along the optimal path step-by-step

### 3. output.txt

* Contains the main output from the A* algorithm

### 4. simulation_output.txt

* Contains the step-by-step simulation output of the truck movement

---

## How to Run

### Run main algorithm:

```bash
python A_star_search.py
```

### Run simulation (optional):

```bash
python A_star_search_testcase.py
```

### Simulation Output (`simulation_output.txt`)

* Step-by-step movement of the truck between locations

---

## Conclusion

The A* Search algorithm efficiently determines the optimal route by combining actual travel cost and heuristic estimates. This makes it suitable for real-world applications such as logistics and navigation systems.
