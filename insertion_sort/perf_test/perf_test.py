import time
import random

from insertion_sort import insertion_sort

sizes = [100, 1000, 10000]

for size in sizes:
    array = random.sample(range(size * 10), size)

    array_copy = array.copy()
    start_time = time.time()
    iterations = insertion_sort(array_copy)
    end_time = time.time()
    insertion_time = end_time - start_time

    print(f"{'Quantidade':<15}{'Tempo':<20}{'Iterações':<20}")
    print(f"{size:<15}{insertion_time:<20.6f}{iterations:<25}")
    print()
