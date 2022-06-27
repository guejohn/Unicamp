def particionar(lista, inicio, fim):
    """
    Dados 'lista', 'inicio' e 'fim', define o pivo como lista[fim] e reoganiza a lista de forma que todos os 
    elementos antes do pivô sejam menores que o pivô e que todos os elementos após o pivô sejam maiores.
    Retorna: a posição do pivô na lista
    """
    pivo = lista[fim]
    posicao_pivo = inicio - 1

    for i in range(inicio, fim):
        
        if lista[i] <= pivo:
            
            posicao_pivo = posicao_pivo + 1
            aux = lista[posicao_pivo]
            lista[posicao_pivo] = lista[i]
            lista[i] = aux
    
    aux = lista[posicao_pivo + 1]
    lista[posicao_pivo + 1] = lista[fim]
    lista[fim] = aux

    return posicao_pivo + 1

def quick_sort(lista, inicio, fim):
    if inicio < fim:
         posicao_pivo = particionar(lista, inicio, fim)
         quick_sort(lista, inicio, posicao_pivo - 1)
         quick_sort(lista, posicao_pivo + 1, fim)

def le_inteiros():
    """
    Lê uma sequência de inteiros e os guarda em uma lista.
    Retorna: lista de inteiros
    """
    lista = list(map(int,input().split()))
    return lista

def mostra_lista(lista):
    """
    Imprime todos os elementos de uma lista separados por " ".
    """
    print(" ".join(str(elemento) for elemento in lista))

def main():
    lista = le_inteiros()
    quick_sort(lista, 0, len(lista)-1)
    mostra_lista(lista)

main()

     
    