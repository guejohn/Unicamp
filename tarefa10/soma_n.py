
def monta_combinacoes(lista_combinacoes, numero, indice_atual, resto_subtracao):
    """
    Calcula e imprime todas as possíveis combinacoes de soma para o número 'numero', cujos termos estão em ordem crescente.
    """

    if resto_subtracao < 0:
        return None

    elif resto_subtracao == 0:

        for j in range(indice_atual):
            if(j + 1 == indice_atual):
                print(lista_combinacoes[j], end="")
            else:
                print(lista_combinacoes[j], end="+")

        print(f"={numero}")
        return None

    if indice_atual != 0:
        numero_anterior = lista_combinacoes[indice_atual - 1]
    else:
        numero_anterior = 1

    for i in range(numero_anterior, numero + 1):
        lista_combinacoes[indice_atual] = i
        monta_combinacoes(lista_combinacoes, numero, indice_atual + 1, resto_subtracao - i)


def main():
    numero = int(input())
    lista_combinacoes = [0 * elemento for elemento in range(numero)]
    monta_combinacoes(lista_combinacoes, numero, 0, numero)

main()
