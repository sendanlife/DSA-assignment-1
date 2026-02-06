import random
import time

n = 100000

# Small range test data (0-10^4)
small_range = {a: random.randint(0, 10**4) for a in range(n)}
small_range_list = list(small_range.items())

# Large range test data (0-10^7)
large_range = {i: random.randint(0, 10**7) for i in range(n)}
large_range_list = list(large_range.items())

def counting_sort(arr):
    min_value = min(v for k, v in arr)
    max_value = max(v for k,v in arr)

    count = [0] * (max_value - min_value + 1)

    # Count occurrences
    for k, v in arr:
        count[v - min_value] += 1

    # Prefix sums
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [None] * len(arr)

    # Build output (stable sort)
    for k, v in reversed(arr):
        count[v - min_value] -= 1
        index = count[v - min_value]
        output[index] = (k, v)

    return output


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:  
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def test_sorting_algorithms():
    datasets = {
        "Small Range (0-10^4)": small_range_list,
        "Large Range (0-10^7)": large_range_list
    }

    for name, data in datasets.items():
        print(f"\nTesting {name} with {n} elements")

        #Counting sort
        start = time.time()
        counting_sort(data.copy())
        print("Count Sort Time:", round(time.time() - start, 4), "seconds")

        # Merge Sort
        start = time.time()
        merge_sort(data.copy())
        print("Merge Sort Time:", round(time.time() - start, 4), "seconds")

test_sorting_algorithms()