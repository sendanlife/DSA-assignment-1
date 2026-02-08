import time
import random

# --- ADT Implementation ---
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class PositionalLinkedList:
    def __init__(self):
        self.head = Node(None)  # Sentinel Node
        self.size = 0
        self.pos_map = {0: self.head}

    def get(self, i):
        if i < 0 or i >= self.size: raise IndexError("Index out of bounds")
        return self.pos_map[i].next.data

    def insert(self, i, data):
        if i < 0 or i > self.size: raise IndexError("Index out of bounds")
        prev_node = self.pos_map[i]
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        self._sync_map(i)

    def remove(self, i):
        if i < 0 or i >= self.size: raise IndexError("Index out of bounds")
        prev_node = self.pos_map[i]
        node_to_remove = prev_node.next
        prev_node.next = node_to_remove.next
        self.size -= 1
        self._sync_map(i)

    def _sync_map(self, start_index):
        # Complexity: O(n) due to updating all subsequent map entries
        curr = self.pos_map[start_index].next
        for idx in range(start_index, self.size):
            self.pos_map[idx + 1] = curr
            curr = curr.next

    def to_list(self):
        result, curr = [], self.head.next
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

# --- Consolidated Testing & Performance Suite ---

def run_merged_tests():
    print("="*105)
    print(f"{'Test Category':<20} | {'Scenario / Operation':<25} | {'Small (100)':<15} | {'Large (100k)':<15} | {'Status / Result'}")
    print("-" * 105)
    
    # --- PART 1: LOGIC & BOUNDARY TESTS ---
    plist = PositionalLinkedList()
    
    # Head & Tail Insert
    plist.insert(0, "Apple")
    plist.insert(1, "Cherry")
    print(f"{'Boundary':<20} | {'Insert Head/Tail':<25} | {'N/A':<15} | {'N/A':<15} | {plist.to_list()}")
    
    # Middle Insert
    plist.insert(1, "Banana")
    print(f"{'Boundary':<20} | {'Middle Insert':<25} | {'N/A':<15} | {'N/A':<15} | {plist.to_list()}")
    
    # Removal
    plist.remove(0) # Remove Apple
    print(f"{'Boundary':<20} | {'Remove Head':<25} | {'N/A':<15} | {'N/A':<15} | {plist.to_list()}")

    # Error Handling
    try:
        plist.get(99)
        err_res = "Fail"
    except IndexError: err_res = "Pass"
    print(f"{'Error Handling':<20} | {'Out of Bounds':<25} | {'N/A':<15} | {'N/A':<15} | {err_res}")

    # Regression
    reg_res = "Pass" if hasattr(plist, 'to_list') else "Fail"
    print(f"{'Regression':<20} | {'Method to_list()':<25} | {'N/A':<15} | {'N/A':<15} | {reg_res}")

    print("-" * 105)
    
    # --- PART 2: EMPIRICAL PERFORMANCE PROOF ---
    small, large = PositionalLinkedList(), PositionalLinkedList()
    # Populate datasets
    for i in range(100000):
        if i < 100: small.insert(i, f"S{i}")
        large.insert(i, f"L{i}")

    def measure(func):
        start = time.perf_counter()
        func()
        return time.perf_counter() - start

    def verify_complexity(t_small, t_large, expected_type):
        # Prevent division by zero if operation is too fast
        safe_small = max(t_small, 1e-9) 
        ratio = t_large / safe_small
        
        if expected_type == "O(1)":
            # For O(1), ratio should be small (allowing for noise, < 10x is safe)
            passed = ratio < 10.0
            status = "PASS" if passed else "FAIL"
            return f"{status}: Ratio {ratio:.1f}x (Exp ~1x)"
            
        elif expected_type == "O(n)":
            # For O(n), ratio should reflect data size increase (100 -> 100k is 1000x)
            # We set a loose threshold (> 100x) to confirm it is definitely not O(1)
            passed = ratio > 100.0
            status = "PASS" if passed else "FAIL"
            return f"{status}: Ratio {ratio:.1f}x (Exp ~1000x)"

    # --- BENCHMARKS ---

    # 1. GET Benchmark (Expected: O(1))
    t_s_get = measure(lambda: small.get(50))
    t_l_get = measure(lambda: large.get(50000))
    res_get = verify_complexity(t_s_get, t_l_get, "O(1)")
    
    print(f"{'Performance':<20} | {'GET Access':<25} | {t_s_get:<15.8f} | {t_l_get:<15.8f} | {res_get}")

    # 2. INSERT Benchmark (Expected: O(n))
    t_s_ins = measure(lambda: small.insert(50, "NEW"))
    t_l_ins = measure(lambda: large.insert(50000, "NEW"))
    res_ins = verify_complexity(t_s_ins, t_l_ins, "O(n)")
    
    print(f"{'Performance':<20} | {'INSERT Scaling':<25} | {t_s_ins:<15.8f} | {t_l_ins:<15.8f} | {res_ins}")

    # 3. REMOVE Benchmark (Expected: O(n))
    t_s_rem = measure(lambda: small.remove(51))
    t_l_rem = measure(lambda: large.remove(50001))
    res_rem = verify_complexity(t_s_rem, t_l_rem, "O(n)")
    
    print(f"{'Performance':<20} | {'REMOVE Scaling':<25} | {t_s_rem:<15.8f} | {t_l_rem:<15.8f} | {res_rem}")

if __name__ == "__main__":
    run_merged_tests()
