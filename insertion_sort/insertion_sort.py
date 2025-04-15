def insertion_sort(unsorted_items):
    item_count = len(unsorted_items)

    for i in range(1, item_count):
        current_value = unsorted_items[i]

        while i > 0 and unsorted_items[i - 1] > current_value:
            unsorted_items[i] = unsorted_items[i - 1]
            i -= 1

        unsorted_items[i] = current_value

        print(f"Iteração {i}: {unsorted_items}")