import sys
import random, time

sys.setrecursionlimit(20000)

n = 1_000_000
arr = [(random.randint(1, 1000), i) for i in range(n)] 

#MergeSort 
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

#QuickSort 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)[0]
    left = [x for x in arr[1:] if x[0] <= pivot] 
    right = [x for x in arr[1:] if x[0] > pivot]
    return quick_sort(left) + [arr[0]] + quick_sort(right)

#Test MergeSort
start = time.time()
sorted_merge = merge_sort(arr)
print("MergeSort time:", time.time() - start)

#Test QuickSort
start = time.time()
sorted_quick = quick_sort(arr)
print("QuickSort time:", time.time() - start)

#Check stability
def is_stable(sorted_arr):
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i-1][0] == sorted_arr[i][0]:
            if sorted_arr[i-1][1] > sorted_arr[i][1]:
                return False
    return True

print("MergeSort stable:", is_stable(sorted_merge))
print("QuickSort stable:", is_stable(sorted_quick))