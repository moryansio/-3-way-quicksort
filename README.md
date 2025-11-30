# 🔢 Sorting App ()

A Python console application for sorting integer vectors.  
The program compares Python’s built-in sorting (`sorted()`) with a custom implementation of **3-way quicksort**.

---

## ✨ Features
- Choose input data source:
  - manual keyboard input;
  - strictly random data;
  - reverse-sorted random data.
- Compare two sorting methods:
  - built-in library sort;
  - custom algorithm implementation.
- Measure execution time and calculate speedup of the built-in sort.
- Smart output:
  - full vector for small arrays;
  - partial output (head and tail) for large arrays.

---

## 📂 Project Structure

sorting_app/
├── main.py                # Entry point: menu and logic
├── sorting_algorithms.py  # 3-way quicksort implementation
├── utils.py               # Data generation and printing
├── benchmarks.py          # Timing and speedup calculation

---

##🖥️ Example

  Enter number of elements: 10
Choose vector type:
1 - manual input
2 - strictly random data
3 - reverse-sorted random data
Your choice: 2

Original vector:
[123, 45, 678, 90, 12, 345, 789, 56, 234, 999]

Sorting results:
Built-in sort:
[12, 45, 56, 90, 123, 234, 345, 678, 789, 999]
Time: 0.000012 sec

Custom sort:
[12, 45, 56, 90, 123, 234, 345, 678, 789, 999]
Time: 0.000034 sec

Built-in sort speedup: 2.83x 
