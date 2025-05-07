import random

def merge_sort(array):
    if len(array) <= 1:
        return array

    meio = len(array) // 2
    metade_esquerda = merge_sort(array[:meio])
    metade_direita = merge_sort(array[meio:])

    return merge(metade_esquerda, metade_direita)

def merge(sublista_esquerda, sublista_direita):
    resultado = []
    indice_esquerda = 0
    indice_direita = 0

    while indice_esquerda < len(sublista_esquerda) and indice_direita < len(sublista_direita):
        if sublista_esquerda[indice_esquerda] <= sublista_direita[indice_direita]:
            resultado.append(sublista_esquerda[indice_esquerda])
            indice_esquerda += 1
        else:
            resultado.append(sublista_direita[indice_direita])
            indice_direita += 1

    resultado.extend(sublista_esquerda[indice_esquerda:])
    resultado.extend(sublista_direita[indice_direita:])

    return resultado

def test():
    sizes = [10, 100, 1000]

    for size in sizes:
        array = random.sample(range(size * 10), size)
        print(f"{size} itens:", merge_sort(array))

test()