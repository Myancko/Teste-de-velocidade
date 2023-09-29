from generate_vector import Generate_vector_10000

def bubble_sort (lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False        

    return lista
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pilha = [(0, len(arr) - 1)]

    while pilha:
        baixo, alto = pilha.pop()
        indice_pivo = particionar(arr, baixo, alto)

        if indice_pivo - 1 > baixo:
            pilha.append((baixo, indice_pivo - 1))
        if indice_pivo + 1 < alto:
            pilha.append((indice_pivo + 1, alto))

    return arr

def particionar(arr, baixo, alto):
    pivo = arr[alto]
    i = baixo - 1

    for j in range(baixo, alto):
        if arr[j] < pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

def Binary_search (lista, x):

    menor = 0
    maior = len(lista) - 1
    meio = 0

    while menor <= maior:

        while menor <= maior:

            meio = menor + (maior - menor)//2

            if lista[meio] == x:
                return meio

            elif lista[meio] < x:
                menor = meio + 1

            else:
                maior = meio - 1

    return print('Elemento foi de b')
