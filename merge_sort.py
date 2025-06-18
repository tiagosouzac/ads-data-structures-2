def merge_sort(items):
    if len(items) <= 1:
        return items
    
    middle = len(items) // 2
    left_items = merge_sort(items[:middle])
    right_items = merge_sort(items[middle:])

    return merge(left_items, right_items)

def merge_sort_iterativo(items):
    step = 1
    length = len(items)

    while step < length:
        for i in range(0, length, 2 * step):
            left = items[i:i + step]
            right = items[i + step:i + 2 * step]
            merged = merge(left, right)

            for j, value in enumerate(merged):
                items[i + j] = value
        
        step *= 2

    return items

def merge(left_items, right_items):
    sorted_items = []
    left_index = 0
    right_index = 0

    while left_index < len(left_items) and right_index < len(right_items):
        if left_items[left_index] <= right_items[right_index]:
            sorted_items.append(left_items[left_index])
            left_index += 1
        else:
            sorted_items.append(right_items[right_index])
            right_index += 1
    
    if left_index < len(left_items):
        sorted_items.extend(left_items[left_index:])

    if right_index < len(right_items):
        sorted_items.extend(right_items[right_index:])
    
    return sorted_items

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
print(merge_sort_iterativo([38, 27, 43, 3, 9, 82, 10]))