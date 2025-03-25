import time
import random

from unoptimized_bubblesort import unoptimized_bubble_sort
from optimized_bubblesort import optimized_bubble_sort

sizes = [100, 1000, 10000]

for size in sizes:
    array = random.sample(range(size * 10), size)

    array_copy = array.copy()
    start_time = time.time()
    unoptimized_iterations = unoptimized_bubble_sort(array_copy)
    end_time = time.time()
    unoptimized_time = end_time - start_time

    array_copy = array.copy()
    start_time = time.time()
    optimized_iterations = optimized_bubble_sort(array_copy)
    end_time = time.time()
    optimized_time = end_time - start_time

    print(f"{'Quantidade':<15}{'Original (s)':<15}{'Iterações (Original)':<25}{'Otimizado (s)':<15}{'Iterações (Otimizado)':<25}")
    print(f"{size:<15}{unoptimized_time:<15.6f}{unoptimized_iterations:<25}{optimized_time:<15.6f}{optimized_iterations:<25}")
    print()
