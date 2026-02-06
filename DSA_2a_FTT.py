import math
import random
import time

#1 Bit reversal   → Prepare data
#2 Butterfly loop → Do the FFT math
#3 Twiddles       → Control frequencies


# Bit reversal

def bit_reversal_permutation(data):

    size = len(data)        # Size of input data
    reversed_index = 0      # Index to hold bit-reversed position

    for current_index in range(1, size):   # Start from second element

        highest_bit = size >> 1  # Highest bit position

        while reversed_index & highest_bit: 
            reversed_index ^= highest_bit   # Clear the bit
            highest_bit >>= 1   # Move to next lower bit

        reversed_index |= highest_bit   # Set the bit

        if current_index < reversed_index:  # Swap only if current_index < reversed_index
            data[current_index], data[reversed_index] = \
                data[reversed_index], data[current_index]



# Twiddles      

def precompute_twiddle_factors(size):

    twiddle_factors = []            #e^-2πik/n -> cos(-2πk/n) + i sin(-2πk/n)

    for k in range(size // 2):

        angle = -2 * math.pi * k / size                 

        twiddle_factors.append(
            complex(math.cos(angle), math.sin(angle))   #rectangular form
        )

    return twiddle_factors


# FFT Algorithm

def fast_fourier_transform_with_count(input_data):

    operation_count = 0         # Count of butterfly operations

    data_size = len(input_data)         # Size of input data

    data = [complex(value) for value in input_data]  # Convert input to complex numbers

    bit_reversal_permutation(data)        # Bit reversal

    twiddle_factors = precompute_twiddle_factors(data_size)  # Precompute twiddles

    current_block_size = 2      # FFT stages

    while current_block_size <= data_size:          

        half_block_size = current_block_size // 2       
        twiddle_step = data_size // current_block_size  # Step size for twiddle factors

        for block_start in range(0, data_size, current_block_size):

            twiddle_index = 0       # Starting index for twiddle factors

            for position in range(half_block_size):

                # Butterfly = main operation
                operation_count += 1

                top_value = data[block_start + position]        # Top element of the butterfly
                bottom_value = data[block_start + position + half_block_size]   # Bottom element of the butterfly

                twiddle = twiddle_factors[twiddle_index]    # Get the twiddle factor

                rotated_bottom = bottom_value * twiddle    # Rotate bottom value

                data[block_start + position] = top_value + rotated_bottom      # Update top element

                data[block_start + position + half_block_size] = top_value - rotated_bottom  # Update bottom element

                twiddle_index += twiddle_step   # Move to next twiddle factor

        current_block_size *= 2  # Double the block size for next stage

    return data, operation_count



def generate_input(size):

    return [random.random() for _ in range(size)]


for power in range(3, 20):   # ensure a good range of sizes

    n = 2 ** power          # easier to handle powers of two

    input_data = generate_input(n)      #generate random input

    data, count = fast_fourier_transform_with_count(input_data)    # get transformed data and operation count

    n_log_n = int(n * math.log2(n))             # nlogn count for comparison

    # Print output till n = 8
    SAMPLE_CASES = 1
    SAMPLE_ENTRIES = 8

    if (power - 3) < SAMPLE_CASES:
        sample_len = min(SAMPLE_ENTRIES, n)
        print(f"Sample input data for n={n} (first {sample_len} entries):")
        for i, v in enumerate(input_data[:sample_len]):
            print(f"  [{i:3d}] {v}")
        print(f"\nSample FFT data for n={n} (first {sample_len} entries):")
        for i, v in enumerate(data[:sample_len]):
            print(f"  [{i:3d}] {v}")

    # Print operation counts
    if power == 3:
        print("Size | Butterflies | n log2(n)")
        print("-" * 35)

    print(f"{n:7d} | {count:11d} | {n_log_n:10d}")


# Time test


def time_test():

    print("Size | Time (seconds)")
    print("-" * 25)

    for power in range(3, 20):  

        n = 2 ** power

        data = generate_input(n)

        start = time.perf_counter()

        fast_fourier_transform_with_count(data)

        end = time.perf_counter()

        print(f"{n:6d} | {end - start:.6f}")


time_test()
