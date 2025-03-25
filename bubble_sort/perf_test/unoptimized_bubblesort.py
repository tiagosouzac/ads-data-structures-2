def unoptimized_bubble_sort(unsorted_items):
    item_count = len(unsorted_items)
    iteration_count = 0

    for i in range(item_count - 1):
        for j in range(item_count - 1 - i):
            iteration_count += 1
            
            if unsorted_items[j] > unsorted_items[j + 1]:
                unsorted_items[j], unsorted_items[j + 1] = unsorted_items[j + 1], unsorted_items[j]

    return iteration_count
