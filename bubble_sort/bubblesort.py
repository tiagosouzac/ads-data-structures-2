def bubble_sort(unsorted_items):
    item_count = len(unsorted_items)

    for i in range(item_count - 1):
        for j in range(item_count - 1 - i):
            if unsorted_items[j] > unsorted_items[j + 1]:
                unsorted_items[j], unsorted_items[j + 1] = unsorted_items[j + 1], unsorted_items[j]
