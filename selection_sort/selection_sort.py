def selection_sort(unsorted_items):
    item_count = len(unsorted_items)

    for i in range(item_count - 1):
        position = i

        for j in range(i + 1, item_count):
            if unsorted_items[j] < unsorted_items[position]:
                position = j

        unsorted_items[i], unsorted_items[position] = unsorted_items[position], unsorted_items[i]  
