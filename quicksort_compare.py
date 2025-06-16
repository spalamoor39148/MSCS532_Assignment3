import random
import time
import sys

sys.setrecursionlimit(100000) # Adjust as needed for your system and input sizes

def randomized_quicksort(arr):
    """
    Sorts a list using the Randomized Quicksort algorithm.
    The pivot element is chosen uniformly at random.

    Args:
        arr: The list to be sorted.

    Returns:
        The sorted list.
    """
    if len(arr) <= 1:
        return arr

    # Choose a random pivot index
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    less = []
    equal = []
    greater = []

    # Partitioning step
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    # Recursive calls
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

def deterministic_quicksort(arr):
    """
    Sorts a list using the Deterministic Quicksort algorithm (first element as pivot).

    Args:
        arr: The list to be sorted.

    Returns:
        The sorted list.
    """
    if len(arr) <= 1:
        return arr

    # Deterministically choose the first element as the pivot
    pivot = arr[0]

    less = []
    equal = []
    greater = []

    # Partitioning step
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    # Recursive calls
    return deterministic_quicksort(less) + equal + deterministic_quicksort(greater)

# --- Array Generation Functions ---

def generate_random_array(size):
    """Generates an array of the given size with random integers."""
    return [random.randint(0, size) for _ in range(size)]

def generate_sorted_array(size):
    """Generates a sorted array of the given size."""
    return list(range(size))

def generate_reverse_sorted_array(size):
    """Generates a reverse-sorted array of the given size."""
    return list(range(size - 1, -1, -1))

def generate_array_with_duplicates(size, num_unique_elements):
    """Generates an array with duplicates."""
    return [random.randint(0, num_unique_elements - 1) for _ in range(size)]

# --- Timing Function ---

def measure_time(sort_func, arr):
    """Measures the execution time of a sorting function."""
    start_time = time.perf_counter() # High-resolution timer
    sort_func(arr)
    end_time = time.perf_counter()
    return end_time - start_time

# --- Empirical Comparison ---

if __name__ == "__main__":
    # Define input sizes to test
    input_sizes = [1000, 5000, 10000] # Adjust as needed

    # Number of runs for averaging
    num_runs = 5

    for size in input_sizes:
        print(f"\n--- Input Size: {size} ---")

        # --- Randomly Generated Arrays ---
        random_times_rand = []
        random_times_det = []
        for _ in range(num_runs):
            arr = generate_random_array(size)
            random_times_rand.append(measure_time(randomized_quicksort, list(arr))) # Use list(arr) to create a copy
            random_times_det.append(measure_time(deterministic_quicksort, list(arr)))

        print(f"Random Array (Randomized Quicksort): {sum(random_times_rand) / num_runs:.6f} seconds (average)")
        print(f"Random Array (Deterministic Quicksort): {sum(random_times_det) / num_runs:.6f} seconds (average)")

        # --- Already Sorted Arrays ---
        sorted_times_rand = []
        sorted_times_det = []
        for _ in range(num_runs):
            arr = generate_sorted_array(size)
            sorted_times_rand.append(measure_time(randomized_quicksort, list(arr)))
            sorted_times_det.append(measure_time(deterministic_quicksort, list(arr)))

        print(f"Sorted Array (Randomized Quicksort): {sum(sorted_times_rand) / num_runs:.6f} seconds (average)")
        print(f"Sorted Array (Deterministic Quicksort): {sum(sorted_times_det) / num_runs:.6f} seconds (average)")

        # --- Reverse-Sorted Arrays ---
        reverse_times_rand = []
        reverse_times_det = []
        for _ in range(num_runs):
            arr = generate_reverse_sorted_array(size)
            reverse_times_rand.append(measure_time(randomized_quicksort, list(arr)))
            reverse_times_det.append(measure_time(deterministic_quicksort, list(arr)))

        print(f"Reverse-Sorted Array (Randomized Quicksort): {sum(reverse_times_rand) / num_runs:.6f} seconds (average)")
        print(f"Reverse-Sorted Array (Deterministic Quicksort): {sum(reverse_times_det) / num_runs:.6f} seconds (average)")

        # --- Arrays with Repeated Elements ---
        duplicates_times_rand = []
        duplicates_times_det = []
        for _ in range(num_runs):
            arr = generate_array_with_duplicates(size, size // 10) # Example: limited unique elements
            duplicates_times_rand.append(measure_time(randomized_quicksort, list(arr)))
            duplicates_times_det.append(measure_time(deterministic_quicksort, list(arr)))

        print(f"Array with Duplicates (Randomized Quicksort): {sum(duplicates_times_rand) / num_runs:.6f} seconds (average)")
        print(f"Array with Duplicates (Deterministic Quicksort): {sum(duplicates_times_det) / num_runs:.6f} seconds (average)")
