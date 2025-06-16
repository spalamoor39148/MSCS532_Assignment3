import random
import time
import matplotlib.pyplot as plt

def randomized_quicksort(arr):
    """
    Sorts a list using the Randomized Quicksort algorithm.
    
    Args:
        arr (list): The list to be sorted.
    
    Returns:
        list: A new sorted list.
    """
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    pivot = random.choice(arr)  # Random pivot selection

    less = []
    equal = []
    greater = []

    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)

    return randomized_quicksort(less) + equal + randomized_quicksort(greater)


def run_test_cases():
    test_cases = {
        "Repeated elements": [3, 6, 8, 10, 1, 2, 1],
        "Empty array": [],
        "Already sorted": [1, 2, 3, 4, 5],
        "Reverse sorted": [5, 4, 3, 2, 1],
        "Random array": [9, 2, 5, 1, 7, 4, 8, 3, 6],
        "Single element": [7],
        "All equal elements": [5, 5, 5, 5, 5]
    }

    for description, arr in test_cases.items():
        print(f"\n{description}:")
        print("Original array:", arr)
        print("Sorted array:  ", randomized_quicksort(arr))


def benchmark_randomized_quicksort():
    """
    Benchmarks the average runtime of Randomized Quicksort on increasing input sizes.
    """
    sizes = [100 * i for i in range(1, 21)]  # Input sizes from 100 to 2000
    times = []

    for n in sizes:
        arr = random.sample(range(n * 10), n)
        start = time.time()
        randomized_quicksort(arr)
        end = time.time()
        times.append(end - start)

    # Plotting the benchmark
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', color='teal')
    plt.title("Randomized Quicksort Runtime vs Input Size")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("=== Randomized Quicksort Test Cases ===")
    run_test_cases()

    print("\n\n=== Benchmarking Randomized Quicksort ===")
    benchmark_randomized_quicksort()
