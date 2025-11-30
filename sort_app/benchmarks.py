import time
from sorting_algorithms import quicksort_3way

def benchmark(arr):
    #Library sort
    start = time.perf_counter()
    sorted_lib = sorted(arr)
    lib_time = time.perf_counter() - start
    #Custom sort
    start = time.perf_counter()
    sorted_custom = quicksort_3way(arr)
    custom_time = time.perf_counter() - start

    #speedup
    speedup = custom_time / lib_time if lib_time > 0 else float('inf')

    return sorted_lib, lib_time, sorted_custom, custom_time, speedup

