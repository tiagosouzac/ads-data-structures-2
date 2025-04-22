def is_in_ascending_order(v):
    if len(v) <= 1:
        return True
    
    for i in range(len(v) - 1):
        if v[i] > v[i + 1]:
            return False
    
    return True


def insert_in_order(x, v):
    result = v.copy()
    
    i = 0
    while i < len(result) and result[i] < x:
        i += 1
    
    result.insert(i, x)
    
    return result


def recursive_insertion_sort(v, n=None):
    if n is None:
        n = len(v)
    
    if n <= 1:
        return v
    
    recursive_insertion_sort(v, n-1)
    
    last = v[n-1]
    j = n - 2
    
    while j >= 0 and v[j] > last:
        v[j+1] = v[j]
        j -= 1
    
    v[j+1] = last
    
    return v


def recursive_selection_sort(v, start=0):
    if start >= len(v) - 1:
        return v
    
    min_index = start
    for i in range(start + 1, len(v)):
        if v[i] < v[min_index]:
            min_index = i
    
    if min_index != start:
        v[start], v[min_index] = v[min_index], v[start]
    
    return recursive_selection_sort(v, start + 1)


def sort_descending(v):
    result = v.copy()
    n = len(result)
    
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if result[j] > result[max_index]:
                max_index = j
        
        if max_index != i:
            result[i], result[max_index] = result[max_index], result[i]
    
    return result


def merge_sort(v):
    if len(v) <= 1:
        return v
    
    middle = len(v) // 2
    left = v[:middle]
    right = v[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result