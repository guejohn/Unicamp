def calcula_maior_elemento(lista_numeros, tamanho_lista):
    """
    Dada uma lista 'lista_numeros', calcula o maior elemento da lista
    Retorna: inteiro
    """
    if tamanho_lista == 1:
        return lista_numeros[0]
    else:
        proximo = calcula_maior_elemento(lista_numeros, tamanho_lista-1)
        if proximo > lista_numeros[tamanho_lista-1]:
            return proximo
        else:
            return lista_numeros[tamanho_lista-1]

def main():
    lista_numeros = list(map(int, input().split()))
    tamanho_lista = len(lista_numeros)
    maior_elemento = calcula_maior_elemento(lista_numeros,tamanho_lista)
    print(maior_elemento)

main()