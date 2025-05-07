# Resultados:

# | Tamanho do Vetor | Tempo Recursivo (s) | Tempo Iterativo (s) |
# | ---------------- | ------------------- | ------------------- |
# | 100              | 0.000147            | 0.000201            |
# | 1.000            | 0.001840            | 0.002435            |
# | 5.000            | 0.010960            | 0.013647            |
# | 10.000           | 0.023205            | 0.028811            |
# | 50.000           | 0.171688            | 0.219442            |
# | 100.000          | 0.288233            | 0.347220            |

# Versão recursiva: o Merge Sort recursivo é mais simples de entender e implementar. Ele expressa diretamente a ideia de dividir para conquistar, o que facilita a escrita e a manutenção do código.
# Versão iterativa: a versão iterativa consome menos memória de pilha e é mais estável para listas muito grandes. Além disso, ela evita o risco de estouro de pilha, o que a torna mais robusta em cenários com grandes volumes de dados.

import time
import random

def merge(array, inicio, meio, fim):
    left = array[inicio:meio+1]
    right = array[meio+1:fim+1]
    
    i = j = 0
    k = inicio

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

def merge_sort_iterativo(array):
    n = len(array)
    tamanho = 1

    while tamanho < n:
        for inicio in range(0, n, 2 * tamanho):
            meio = min(inicio + tamanho - 1, n - 1)
            fim = min(inicio + 2 * tamanho - 1, n - 1)

            if meio < fim:
                merge(array, inicio, meio, fim)
        tamanho *= 2

def merge_sort_recursivo(array):
    if len(array) > 1:
        mid = len(array) // 2
        L = array[:mid]
        R = array[mid:]

        merge_sort_recursivo(L)
        merge_sort_recursivo(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

tamanhos = [100, 1000, 5000, 10000, 50000, 100000]
resultados = []

for tamanho in tamanhos:
    array_base = [random.randint(0, 10**6) for _ in range(tamanho)]
    
    arr1 = array_base.copy()
    inicio = time.perf_counter()
    merge_sort_recursivo(arr1)
    tempo_recursivo = time.perf_counter() - inicio

    arr2 = array_base.copy()
    inicio = time.perf_counter()
    merge_sort_iterativo(arr2)
    tempo_iterativo = time.perf_counter() - inicio

    resultados.append((tamanho, tempo_recursivo, tempo_iterativo))

for resultado in resultados:
    print(f"Itens: {resultado[0]}, Recursivo: {resultado[1]:.6f}s, Iterativo: {resultado[2]:.6f}s")
