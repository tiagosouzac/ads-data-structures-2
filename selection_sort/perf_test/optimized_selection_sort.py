def optimized_selection_sort(unsorted_items):
    item_count = len(unsorted_items)
    iteration_count = 0

    for i in range(item_count - 1):
        position = i

        for j in range(i + 1, item_count):
            iteration_count += 1
            
            if unsorted_items[j] < unsorted_items[position]:
                position = j

        if position != i:
            unsorted_items[i], unsorted_items[position] = unsorted_items[position], unsorted_items[i]

    return iteration_count
