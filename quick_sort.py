def quick_sort(items):
    if len(items) <= 1:
        return items

    pivot = items[0]
    less = []
    greater = []
    
    for i in range(1, len(items)):
        if items[i] <= pivot:
            less.append(items[i])
        else:
            greater.append(items[i])
    
    return quick_sort(less) + [pivot] + quick_sort(greater)

def quicksort_com_partition(array, left, right):
    # Se ainda há elementos para ordenar
    if left < right:
        # Encontra a posição correta do pivô
        pivot_position = partition(array, left, right)
        
        # Ordena a parte esquerda (elementos menores que o pivô)
        quicksort_com_partition(array, left, pivot_position - 1)
        
        # Ordena a parte direita (elementos maiores que o pivô)
        quicksort_com_partition(array, pivot_position + 1, right)

def partition(array, left, right):
    # Escolhe o último elemento como pivô
    pivot = array[right]
    
    # Índice do último elemento menor que o pivô
    smaller_index = left - 1
    
    # Percorre todos os elementos exceto o pivô
    for current in range(left, right):
        # Se o elemento atual é menor ou igual ao pivô
        if array[current] <= pivot:
            # Move o índice dos menores
            smaller_index += 1
            # Troca o elemento atual com o elemento na posição dos menores
            array[smaller_index], array[current] = array[current], array[smaller_index]
    
    # Coloca o pivô na posição correta
    array[smaller_index + 1], array[right] = array[right], array[smaller_index + 1]
    
    # Retorna a posição final do pivô
    return smaller_index + 1

def quick_sort_2(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    less = [x for x in array[1:] if x <= pivot]
    greater = [x for x in array[1:] if x > pivot]
    
    return quick_sort_2(less) + [pivot] + quick_sort_2(greater)

def quick_sort_iterativo(array):
    """
    Implementação iterativa do Quick Sort usando uma pilha (stack)
    para simular as chamadas recursivas.
    """
    if len(array) <= 1:
        return array
    
    # Cria uma cópia do array para não modificar o original
    arr = array.copy()
    
    # Pilha para armazenar os índices de início e fim das sub-arrays
    stack = [(0, len(arr) - 1)]
    
    while stack:
        # Remove o último par de índices da pilha
        left, right = stack.pop()
        
        # Se ainda há elementos para ordenar nesta sub-array
        if left < right:
            # Particiona a sub-array e obtém a posição do pivô
            pivot_position = partition(arr, left, right)
            
            # Adiciona as duas sub-arrays à pilha para processamento posterior
            # Sub-array da esquerda (elementos menores que o pivô)
            stack.append((left, pivot_position - 1))
            
            # Sub-array da direita (elementos maiores que o pivô)
            stack.append((pivot_position + 1, right))
    
    return arr

def quick_sort_iterativo_inplace(array):
    """
    Implementação iterativa do Quick Sort que modifica o array original (in-place).
    """
    if len(array) <= 1:
        return
    
    # Pilha para armazenar os índices de início e fim das sub-arrays
    stack = [(0, len(array) - 1)]
    
    while stack:
        # Remove o último par de índices da pilha
        left, right = stack.pop()
        
        # Se ainda há elementos para ordenar nesta sub-array
        if left < right:
            # Particiona a sub-array e obtém a posição do pivô
            pivot_position = partition(array, left, right)
            
            # Adiciona as duas sub-arrays à pilha para processamento posterior
            # Sub-array da esquerda (elementos menores que o pivô)
            stack.append((left, pivot_position - 1))
            
            # Sub-array da direita (elementos maiores que o pivô)
            stack.append((pivot_position + 1, right))

# Exemplos de uso:
print("=== Quick Sort Recursivo ===")
arr1 = [38, 27, 43, 3, 9, 82, 10]
print("Array original:", arr1)
resultado1 = quick_sort(arr1)
print("Array ordenado (recursivo):", resultado1)

print("\n=== Quick Sort com Partition (in-place) ===")
arr2 = [38, 27, 43, 3, 9, 82, 10]
print("Array original:", arr2)
quicksort_com_partition(arr2, 0, len(arr2) - 1)
print("Array ordenado (in-place):", arr2)

print("\n=== Quick Sort Iterativo ===")
arr3 = [38, 27, 43, 3, 9, 82, 10]
print("Array original:", arr3)
resultado3 = quick_sort_iterativo(arr3)
print("Array ordenado (iterativo):", resultado3)

print("\n=== Quick Sort Iterativo In-Place ===")
arr4 = [38, 27, 43, 3, 9, 82, 10]
print("Array original:", arr4)
quick_sort_iterativo_inplace(arr4)
print("Array ordenado (iterativo in-place):", arr4)