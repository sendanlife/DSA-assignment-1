import math

#calculate distance between two nodes
def get_distance(node1, node2):
    return math.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)

#reverse the tour between two indices
def two_opt_swap(tour, i, j):
    #tour[i+1:j+1] takes the segment, [::-1] reverses it
    new_tour = tour[0:i+1] + tour[i+1:j+1][::-1] + tour[j+1:]
    return new_tour

#run 2-opt optimization
def run_2opt(targets, tour):
    n = len(tour)
    improved = True
    while improved:
        improved = False
        for i in range(n - 2): #ensure at least two edges to swap
            for j in range(i + 2, n):
                idx_a, idx_b = tour[i], tour[i + 1]
                idx_c = tour[j]
                idx_d = tour[(j + 1) % n] #wrap around to start

                d1 = get_distance(targets[idx_a], targets[idx_b]) + get_distance(targets[idx_c], targets[idx_d])
                
                d2 = get_distance(targets[idx_a], targets[idx_c]) + get_distance(targets[idx_b], targets[idx_d])

                if d2 < d1:
                    tour = two_opt_swap(tour, i, j)
                    improved = True

    return tour

#calculate total distance of the tour
def calculate_total_distance(tour, targets):
    total = 0
    n = len(tour)
    for i in range(n):
        current_city = tour[i]
        next_city = tour[(i + 1) % n] #wrap around to start
        total += get_distance(targets[current_city], targets[next_city])
    return total

def run_test():
    test_cases = [
        {
            "name": "The Hexagon",
            "targets": {
                0: (0, 2),
                1: (2, 4),
                2: (4, 4),
                3: (6, 2),
                4: (4, 0),
                5: (2, 0)
            },
            "initial_tour": [0, 3, 1, 4, 2, 5]
        },
        {
            "name": "The Line",
            "targets": {
                0: (0, 0),
                1: (2, 0),
                2: (4, 0),
                3: (6, 0),
                4: (8, 0)
            },
            "initial_tour": [0, 4, 1, 3, 2]
        },
        {
            "name": "The Twin Clusters",
            "targets": {
                0: (0, 0),
                1: (0, 2),
                2: (2, 0),
                3: (2, 2),
                4: (10, 0),
                5: (10, 2),
                6: (12, 0),
                7: (12, 2),
            },
            "initial_tour": [0, 4, 1, 5, 2, 6, 3, 7]
        }
    ]

    for case in test_cases:
        print(f"\n--- Testing: {case['name']} ---")
        targets = case["targets"]
        tour = case["initial_tour"]

        dist_start = calculate_total_distance(tour, targets)
        print(f"Initial Tour: {tour}")

        optimised_tour = run_2opt(targets, tour)

        dist_end = calculate_total_distance(optimised_tour, targets)
        print(f"Optimised Tour: {optimised_tour}")
        print(f"Total Distance: {dist_end:.2f}")
        print(f"Distance Improvement: {dist_start - dist_end:.2f}")

if __name__ == "__main__":
    run_test()
    
''' 4 cities with their (x, y) coordinates
#setup test case
targets = { #A, B, C, D
    0: (0, 0),
    1: (0, 1),
    2: (1, 1),
    3: (1, 0)
}
locations = targets 
initial_tour = [0, 2, 1, 3] #Initial tour A -> C -> B -> D
print(f"Initial Tour: {initial_tour}")

#run 2-opt optimisation
optimised_tour = run_2opt(locations, initial_tour)
print(f"Optimised Tour: {optimised_tour}")

#calculate total distance before optimisation
dist_before = calculate_total_distance(initial_tour, locations)

#calculate total distance of the tour
total_dist = calculate_total_distance(optimised_tour, locations)

#print results
print(f"Total Distance: {total_dist:2f}")
print(f"Improvement: { dist_before - total_dist:.2f}") '''