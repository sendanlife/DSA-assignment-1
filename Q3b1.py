import random
import time

n = 10
n_large = 100

# Small range test data (0-10^2)
small_range = {a: random.randint(0, 10**2) for a in range(n)}
small_range_list = list(small_range.items())

# Large range test data (0-10^4)
large_range = {i: random.randint(0, 10**4) for i in range(n)}
large_range_list = list(large_range.items())

# Small range test data (0-10^2)
small_range_large_n = {a: random.randint(0, 10**2) for a in range(n_large)}
small_range__large_n_list = list(small_range_large_n.items())

# Large range test data (0-10^4)
large_range_large_n = {i: random.randint(0, 10**4) for i in range(n_large)}
large_range_large_n_list = list(large_range_large_n.items())

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_min_indx = i
        for j in range(i +1, len(arr)):
            if arr[j] < arr[cur_min_indx]:
                cur_min_indx = j

        arr[i], arr[cur_min_indx] = arr[cur_min_indx], arr[i]


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
        "Small Range (0-10^2)": small_range_list,
        "Large Range (0-10^4)": large_range_list
    }

    for name, data in datasets.items():
        print(f"\nTesting {name} with {n} elements")

        #Selection sort
        start = time.time()
        selection_sort(data.copy())
        print("Selection Sort Time:", round(time.time() - start, 4), "seconds")

        # Merge Sort
        start = time.time()
        merge_sort(data.copy())
        print("Merge Sort Time:", round(time.time() - start, 4), "seconds")

    #For large elements
    datasets = {
        "Small Range (0-10^2)": small_range__large_n_list,
        "Large Range (0-10^4)": large_range_large_n_list
    }
    for name, data in datasets.items():
        print(f"\nTesting {name} with {n_large} elements")

        #Selection sort
        start = time.time()
        selection_sort(data.copy())
        print("Selection Sort Time:", round(time.time() - start, 4), "seconds")

        # Merge Sort
        start = time.time()
        merge_sort(data.copy())
        print("Merge Sort Time:", round(time.time() - start, 4), "seconds")

test_sorting_algorithms()
