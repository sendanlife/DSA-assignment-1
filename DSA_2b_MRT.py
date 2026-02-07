import math
import random

# 3T(n/2) + lgn

def recursive(n):

    if n == 0:
        return 0
    
    if n == 1:
        return 1 + int(math.log2(n))
    
    if n == 2:
        return 2 + int(math.log2(n))

    part1 = n // 2
    part2 = n // 2
    part3 = n // 2

    # Recursive calls
    cost1 = recursive(part1)
    cost2 = recursive(part2)
    cost3 = recursive(part3)

    levels = int(math.log2(n))

    total_op = cost1 + cost2 + cost3 + levels
    return total_op

print("\n=== Algorithm Growth Analysis ===")
print(f"{'n':>8} | {'Operation Cost':>15}")
print("-" * 33)

for pow in range(3, 17): 

    n = 2 ** pow

    cost = recursive(n)

    print(f"{n:8d} | {cost:15d}")

    









#Singapore Context

start = "Toa Payoh"

# NSL + Stops

station_distance = {
    "Jurong East": 17,
    "Ang Mo Kio": 3,
    "Bishan": 2,
    "Toa Payoh": 0,
    "Orchard": 3,
    "City Hall": 7,
    "Raffles Place": 8,
    "Somerset": 4,
    "Yishun": 6,
    "Woodlands": 10,
    "Kranji": 12
}

# Travel Time Estimator

def estimate_travel_time(stops):

    avg_time_per_stop = 1
    waiting_time = random.randint(0, 6)
    random_delay = random.randint(0, 3)

    time = (stops * avg_time_per_stop) + waiting_time + random_delay

    return int(round(time))

# Fare Constants

cost_per_stop = 0.30
cost_per_min = 0.06

# Fare Calculator

def calculate_fare(destination, travel_time):

    stops = abs(
        station_distance[destination] -
        station_distance[start]
    )

    fare = (stops * cost_per_stop) + (travel_time * cost_per_min)

    return round(fare, 2)

#Recursion

def process_logs(logs):

    n = len(logs)

    # Empty
    if n == 0:
        return 0.0, 0

    # Base case
    if n == 1:
        return logs[0]["fare"], 1

    if n == 2:
        fare = logs[0]["fare"] + logs[1]["fare"]
        cost = 2 + int(math.log2(n))
        return fare, cost

    half = n // 2

    part1 = logs[:half]
    part2 = logs[half:]

    # Overlapping middle part
    start_index = half // 2
    end_index = start_index + half

    part3 = logs[start_index:end_index]

    # Recursive calls
    f1, c1 = process_logs(part1)
    f2, c2 = process_logs(part2)
    f3, c3 = process_logs(part3)

    # Merge cost
    merge_cost = int(math.log2(n))

    total_fare = f1 + f2 + f3
    total_cost = c1 + c2 + c3 + merge_cost

    return total_fare, total_cost

# Database

stations = list(station_distance.keys())
stations.remove(start)


def generate_logs(n):

    database = []

    for i in range(n):

        passenger_id = 1000 + i

        destination = random.choice(stations)

        hour = random.randint(5, 23)
        minute = random.randint(0, 59)

        time_str = f"{hour}:{minute:02}"

        stops = abs(
            station_distance[destination] -
            station_distance[start]
        )

        travel_time = estimate_travel_time(stops)

        fare = calculate_fare(destination, travel_time)


        record = {
            "id": passenger_id,
            "from": start,
            "to": destination,
            "time": time_str,
            "stops": stops,
            "travel_time": travel_time,
            "fare": fare
        }

        database.append(record)

    return database


# Growth Table

def run_cost_analysis():

    print("\n=== MRT Fare Algorithm Growth Analysis ===")
    print(f"{'n':>8} | {'Operation Cost':>15}")
    print("-" * 33)

    for power in range(3, 17): 

        n = 2 ** power

        logs = generate_logs(n)

        _, cost = process_logs(logs)

        print(f"{n:8d} | {cost:15d}")


# Main Run

logs = generate_logs(64)

total_fare, cost = process_logs(logs)

run_cost_analysis()

print("\n=== Sample Transport Database (First 10 Records) ===")

for record in logs[:10]:
    print(record)

print("\n=== North-South Line Transport Analysis ===")

print("Total Fare Collected: $", round(total_fare, 2))
print("Operation Cost:", cost)

