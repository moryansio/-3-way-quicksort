from utils import generate_random_vector, generate_reverse_sorted_vector, print_vector
from benchmarks import benchmark

def main():
    n = int(input("Enter the size of the array to sort: "))
    print("Choose the type of array to generate:")
    print("1. Enter keyboard input")
    print("2. Random array")
    print("3. Reverse sorted random array")
    choice = int(input("Your choice: "))

    if choice == 1:
        arr = list(map(int, input("Enter the elements separated by spaces: ").split()))
    elif choice == 2:
        arr = generate_random_vector(n)
    elif choice == 3:
        arr = generate_reverse_sorted_vector(n)
    else:
        print("Invalid choice.")
        return
    
    print("Original array:")
    print_vector(arr)

    sorted_lib, lib_time, sorted_custom, custom_time, speedup = benchmark(arr)

    print("\nSort results:")
    print("Library sorted array:")
    print_vector(sorted_lib)
    print(f"Library sort time: {lib_time:.6f} seconds")

    print("\nCustom sorted array:")
    print_vector(sorted_custom)
    print(f"Custom sort time: {custom_time:.6f} seconds")

    print(f"\nSpeedup (Custom / Library): {speedup:.2f}x")

if __name__ == "__main__":
    main()