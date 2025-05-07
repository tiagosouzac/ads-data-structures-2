# a) Não. Em listas pequenas, a diferença no cálculo do meio muda levemente como a divisão é feita, mas o resultado final ainda é a lista ordenada corretamente, na maioria dos casos.

# b) Não. Ao utilizar variações diferentes para o cálculo do meio, o algoritmo pode deixar de funcionar corretamente. Em especial, a variação (inicio + fim + 1) // 2 pode fazer com que o valor de meio não reduza o tamanho das sublistas corretamente, levando a chamadas recursivas com os mesmos parâmetros. Isso faz com que a recursão nunca atinja o caso base, causando erro de recursão infinita (estouro de pilha). Mesmo a variação (inicio + fim - 1) // 2 pode desequilibrar as divisões, o que não quebra o algoritmo diretamente, mas pode afetar o desempenho em alguns casos.

# c) Sim, a variação `(inicio + fim + 1) // 2` pode provocar falha ou erro de recursão infinita. Quando você puxa o meio para a direita e faz a chamada recursiva para merge_sort(array, inicio, meio), pode acontecer do meio ser igual ao fim, especialmente quando a lista tem poucos elementos. Isso faz com que a sublista não diminua em tamanho, e o algoritmo entra em recursão infinita.

import random

def merge_sort(array, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim + 1) // 2
        merge_sort(array, inicio, meio)
        merge_sort(array, meio + 1, fim)
        merge(array, inicio, meio, fim)

    return array

def merge(array, inicio, meio, fim):
    sublista_esquerda = array[inicio:meio + 1]
    sublista_direita = array[meio + 1:fim + 1]

    indice_esquerda = 0
    indice_direita = 0
    indice_geral = inicio

    while indice_esquerda < len(sublista_esquerda) and indice_direita < len(sublista_direita):
        if sublista_esquerda[indice_esquerda] <= sublista_direita[indice_direita]:
            array[indice_geral] = sublista_esquerda[indice_esquerda]
            indice_esquerda += 1
        else:
            array[indice_geral] = sublista_direita[indice_direita]
            indice_direita += 1
        indice_geral += 1

    while indice_esquerda < len(sublista_esquerda):
        array[indice_geral] = sublista_esquerda[indice_esquerda]
        indice_esquerda += 1
        indice_geral += 1

    while indice_direita < len(sublista_direita):
        array[indice_geral] = sublista_direita[indice_direita]
        indice_direita += 1
        indice_geral += 1

def test():
    sizes = [10, 100, 1000]

    for size in sizes:
        array = random.sample(range(size * 10), size)
        print(f"{size} itens:", merge_sort(array, 0, size))

print(merge_sort([38, 27, 43, 3, 9, 82, 10], 0, 7))