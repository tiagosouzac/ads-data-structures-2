def merge_sort(array):
    if len(array) <= 1:
        return array
    
    middle = len(array) // 2
    left = merge_sort(array[middle:])
    right = merge_sort(array[:middle])
    
    return merge(left, right)

def merge(left, right):
    sorted = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted.append(left[left_index])
            left_index += 1
        else:
            sorted.append(right[right_index])
            right_index += 1
    
    sorted.extend(left[left_index:])
    sorted.extend(right[right_index:])

    return sorted

def quick_sort(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        quick_sort(array, left, pivot - 1)
        quick_sort(array, pivot + 1, right)

def partition(array, left, right):
    pivot = array[right]
    smaller_position = left - 1

    for i in range(left, right):
        if array[i] <= pivot:
            smaller_position += 1
            array[smaller_position], array[i] = array[i], array[smaller_position]
    
    array[smaller_position + 1], array[right] = array[right], array[smaller_position + 1]

    return smaller_position + 1

print(merge_sort([12, 3, 6, 60, 40, 20]))

array = [12, 3, 6, 60, 40, 20]
quick_sort(array, 0, len(array) - 1)
print(array)
