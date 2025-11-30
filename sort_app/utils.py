import random

def generate_random_vector(n):
    return [random.randint(0, 1000) for _ in range(n)]

def generate_reverse_sorted_vector(n):
    vec = generate_random_vector(n)
    return sorted(vec, reverse=True)

def print_vector(vec, limit=20):
    if len (vec) <= limit:
        print(vec)
    else:
        print(vec[:limit], "...", vec[-limit:])