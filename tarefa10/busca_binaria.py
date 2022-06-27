def busca_binaria(lista_numeros,numero, limitante_inferior, limitante_superior):
    """
    Dado uma lista de inteiros em ordem crescente e um número, realiza uma busca binária e retorna o índice da posição desse número
    na lista ou -1 se esse número não estiver na lista.
    """
    meio = (limitante_inferior+limitante_superior)//2

    if limitante_superior >= limitante_inferior:

        if numero == lista_numeros[meio]:
            return meio
        
        elif numero > lista_numeros[meio]:
                return busca_binaria(lista_numeros,numero, meio+1, limitante_superior)
        else:
            return busca_binaria(lista_numeros,numero, limitante_inferior, meio-1)
    else:
        return -1

def main():
    lista_numeros = list(map(int, input().split()))
    numero = int(input())
    limitante_inferior = 0
    limitante_superior = len(lista_numeros)-1
    indice_numero = busca_binaria(lista_numeros,numero, limitante_inferior, limitante_superior)
    print(indice_numero)

main()