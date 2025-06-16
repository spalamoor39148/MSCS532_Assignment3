
# 📄 README

## Project: **Analysis of Randomized Quicksort and Hashing with Chaining**

---

## How to Run the Code

This assignment primarily contains Python code and theoretical analysis and empirical results. 

### Requirements
- Python 3.x 
- For Python: install packages using `pip install matplotlib numpy` (if plotting or benchmarking)
- A code file named something like `randomized_quicksort.py` or `universal_hash_table.py`

### Run Quicksort Benchmarks (Python example):
```bash
python randomized_quicksort.py
```

### Run Hash Table Analysis:
```bash
python universal_hash_table.py
```



---

## Summary of Findings

###  Randomized Quicksort

- **Average-Case Time Complexity**: Proven to be **O(n log n)**.
- **Methodologies**:
  - **Indicator Random Variables**: Analyzes expected number of comparisons based on random pivot placement.
  - **Recurrence Relation**: Confirms expected runtime using recurrence and integration techniques.

### Empirical Insights

- **Random Arrays**: Randomized and deterministic both perform well.
- **Sorted/Reverse-Sorted Arrays**:
  - Randomized: Fast.
  - Deterministic: Exhibits worst-case **O(n²)** behavior.
- **Arrays with Duplicates**: Deterministic may be slightly faster for small inputs.

### Conclusion

Randomized Quicksort is more consistent and avoids worst-case performance. Deterministic Quicksort should avoid using the first element as the pivot.

---

###  Hashing with Chaining

- **Expected Time Complexities** (under Simple Uniform Hashing):
  - **Search (success/failure)**: `O(1 + α)`
  - **Insert**: `O(1)` (amortized)
  - **Delete**: `O(1 + α)`
  - Where `α = n / m` is the load factor.

- **Impact of Load Factor**:
  - Small `α`: Constant-time operations.
  - Large `α`: Linear-time degradation.

- **Strategies to Maintain Low α**:
  - **Dynamic Resizing**: Rehash when `α` exceeds threshold (e.g., 0.7).
  - **Good Hash Functions**: Use universal hashing to minimize clustering.
  - **Collision Resolution**:
    - Chaining: Linked lists per bucket.
    - Open Addressing: Linear/quadratic probing or double hashing.

---

## Recommendations

- **Use Randomized Quicksort** for robust performance across inputs.
- **Avoid naive deterministic pivoting** (like always using the first element).
- **Use dynamic resizing and good hashing** to keep hash operations efficient.
