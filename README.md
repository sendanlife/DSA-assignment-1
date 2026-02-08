# DSA Assignment 1

This repository contains implementations and performance analyses of various Data Structures and Algorithms (DSA) concepts, including custom Linked Lists, the Travelling Salesperson Problem (TSP), Fast Fourier Transform (FFT), Recursion, and Sorting Algorithms.


## Group: P5T3
### Team Members:
* Charissa Koh Yi En (2501810)
* Liew Hui Zhong (2502222)
* Ong Si Kai (2501225)
* Javier Soh Jie En (2500119)
* Syafiq Bin Iskandar Abdullah Yeoh (2500818)
* Clifton Ng Jun Heng (2503193)


## Repository Structure

### 🔹 Question 1: Data Structures
* **`Q1.py`**: Implementation of a **Positional Linked List**.
    * **Features**: Implements a Singly Linked List enhanced with a Python dictionary (`pos_map`) to map indices to nodes.
    * **Performance**: Achieves **O(1)** time complexity for `get()` operations (random access) while maintaining **O(n)** for `insert` and `remove` operations due to map synchronisation.
    * **Testing**: Includes a consolidated test suite checking boundary conditions, error handling, and empirical performance benchmarks comparing Small (100 elements) vs. Large (100k elements) datasets.

### 🔹 Question 2: Algorithms & Analysis
* **`Q2a-expo.py`**: **Traveling Salesperson Problem (TSP) Optimization**.
    * **Algorithm**: Implements the **2-opt heuristic** to optimize tours.
    * **Features**: Includes a `run_2opt` function that iteratively swaps edges to reduce total tour distance.
    * **Test Cases**: Validates against scenarios like "The Hexagon", "The Line", and "The Twin Clusters".

* **`Q2a_FFT.py`**: **Fast Fourier Transform (FFT)**.
    * **Algorithm**: A recursive implementation of the Cooley-Tukey FFT algorithm.
    * **Components**: Handles bit-reversal permutation, precomputed twiddle factors, and the "butterfly" operation.
    * **Analysis**: Compares the operation count against the theoretical $n \log n$ complexity and measures execution time for input sizes up to $2^{19}$.

* **`Q2b_MRT.py`**: **Recursion & Growth Analysis**.
    * **Context**: Simulates Singapore MRT fare calculations (North-South Line) and travel time estimation.
    * **Algorithm**: Analyzes the growth of a recursive function $T(n) = 3T(n/2) + \log n$.
    * **Simulation**: Generates passenger logs with random entry/exit points and calculates fares based on distance and time.

### 🔹 Question 3: Sorting Algorithms
* **`Q3a.py`**: **Merge Sort vs. Quick Sort**.
    * **Comparison**: Benchmarks execution time for sorting 1,000,000 integers.
    * **Stability Check**: Verifies whether the implementations preserve the relative order of equal elements (Merge Sort is stable; this Quick Sort implementation is not).

* **`Q3b1.py`**: **Selection Sort vs. Merge Sort**.
    * **Scenario**: Tests performance on Small ($0-10^2$) vs. Large ($0-10^4$) data ranges.
    * **Goal**: Demonstrates how $O(n^2)$ algorithms (Selection Sort) perform significantly worse than $O(n \log n)$ algorithms (Merge Sort) as dataset size increases.

* **`Q3b2.py`**: **Counting Sort vs. Merge Sort**.
    * **Scenario**: Tests performance on Small ($0-10^4$) vs. Large ($0-10^7$) data ranges.
    * **Goal**: Highlights the efficiency of Counting Sort ($O(n+k)$) when the range of input values ($k$) is small relative to $n$.

## Usage

You can run any of the scripts directly using Python. Each script includes a `main` block or test driver that automatically executes benchmarks when run.

```bash
# Run the Positional Linked List tests
python Q1.py

# Run TSP 2-opt optimization
python Q2a-expo.py

# Run FFT performance analysis
python Q2a_FFT.py

# Run Sorting benchmarks
python Q3a.py
