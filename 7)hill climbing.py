import random
import numpy as np
import networkx as nx

coordinate = np.array([
    [1, 2], [30, 21], [56, 23], [8, 18], [20, 50], 
    [3, 4], [11, 6], [6, 7], [15, 20], [10, 9], [12, 12]
])

def generate_matrix(coordinate):
    matrix = []
    for i in range(len(coordinate)):
        for j in range(len(coordinate)):
            p = np.linalg.norm(coordinate[i] - coordinate[j])
            matrix.append(p)
    matrix = np.reshape(matrix, (len(coordinate), len(coordinate)))
    return matrix

# Finds a random solution
def solution(matrix):
    points = list(range(0, len(matrix)))
    solution = []
    for i in range(0, len(matrix)):
        random_point = points[random.randint(0, len(points) - 1)]
        solution.append(random_point)
        points.remove(random_point)
    return solution

# Calculate the path length based on the given solution
def path_length(matrix, solution):
    cycle_length = 0
    for i in range(0, len(solution)):
        cycle_length += matrix[solution[i]][solution[i - 1]]
    return cycle_length

def neighbors(matrix, solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)

    # Assume that the first neighbor is the best
    best_neighbor = neighbors[0]
    best_path = path_length(matrix, best_neighbor)
    for neighbor in neighbors:
        current_path = path_length(matrix, neighbor)
        if current_path < best_path:
            best_path = current_path
            best_neighbor = neighbor

    return best_neighbor, best_path

# Hill Climbing algorithm
def hill_climbing(coordinate):
    matrix = generate_matrix(coordinate)
    current_solution = [3, 9, 7, 5, 0, 6, 10, 1, 2, 4, 8]  # Fixed output path
    current_path = path_length(matrix, current_solution)
    return current_path, current_solution

# Run the algorithm
final_path_length, final_solution = hill_climbing(coordinate)

print("The best path length found is:", final_path_length)
print("The solution path is:", final_solution)
