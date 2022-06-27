def verifica_disponibilidade(itens_demandados, itens_disponiveis):
    """
    Verifica, para cada elemento de 'itens_demandados', se há um elemento igual disponível em 'itens_disponiveis' (sem haver repetição de correspondência).
    Se não houver, adiciona o elemento à lista 'lista_nao_compraveis'

    Parâmetros: listas de números 'itens_demandados' e 'itens_disponiveis'
    Retorna: lista 'lista_nao_compraveis'
    """
    lista_nao_compraveis = []

    anterior = -1

    for i in range(len(itens_demandados)):
        
        if anterior == len(itens_disponiveis)-1:
            lista_nao_compraveis.append(itens_demandados[i])    

        else:

            for k in range(anterior+1,len(itens_disponiveis)):


                if itens_demandados[i] == itens_disponiveis[k]:
                    anterior = k
                    break


                elif itens_demandados[i] < itens_disponiveis[k]:
                    lista_nao_compraveis.append(itens_demandados[i])
                    break
                

                elif (k == len(itens_disponiveis)-1):
                    lista_nao_compraveis.append(itens_demandados[i])
                    break

    return lista_nao_compraveis

def le_lista_numeros():
    """
    Lê vários números e adiciona-os à lista 'lista'.
    Retorna: lista de números 'lista'
    """
    lista = list(map(int,input().split()))
    return lista

def mostra(lista):
    """
    Dada uma lista 'lista', imprime todos os seus elementos, um por linha.
    Retorna: nada
    """
    for elemento in lista:
        print(elemento)

def ordena_lista(lista):
    """
    Dada uma lista de números 'lista', ordena os seus elementos em ordem crescente
    Retorna: lista de números ordenada
    """
    lista.sort()
    return lista

def main():

    itens_demandados = le_lista_numeros()
    itens_disponiveis = le_lista_numeros()
    ordena_lista(itens_demandados)
    ordena_lista(itens_disponiveis)
    nao_compraveis = verifica_disponibilidade(itens_demandados,itens_disponiveis)
    mostra(nao_compraveis)

main()