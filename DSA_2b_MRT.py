import math
import random


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

# Fare constants

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


# Recursion for Calculation

def process_logs(logs):

    n = len(logs)

    if n == 0:      # Empty case
        return 0, 0.0, 0

    if n == 1:      # Base case
        return 1, logs[0]["fare"], 1

    if n == 2:      # Two records
        fare = logs[0]["fare"] + logs[1]["fare"]
        cost = 2 + int(math.log2(n))
        return 2, fare, cost
    
    half = n // 2           # Divide into 3 parts

    part1 = logs[:half]
    part2 = logs[half:half * 2]
    part3 = logs[half * 2:]
    
    p1, f1, c1 = process_logs(part1)    # Recursive calls
    p2, f2, c2 = process_logs(part2)
    p3, f3, c3 = process_logs(part3)
    
    merge_cost = int(math.log2(n))  # Merge cost
    
    passengers = p1 + p2 + p3
    fare = f1 + f2 + f3
    cost = c1 + c2 + c3 + merge_cost    # Combine results

    return passengers, fare, cost


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

        # Create record
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


# Run & Output

logs = generate_logs(64)

passengers, total_fare, cost = process_logs(logs)

print("\n=== Sample Transport Database (First 10 Records) ===")

for record in logs[:10]:
    print(record)


print("=== North-South Line Transport Analysis ===")
print("Total Passengers:", passengers)
print("Total Fare Collected: $", round(total_fare, 2))
print("Operation Cost:", cost)