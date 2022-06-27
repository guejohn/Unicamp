def ordena(lista, maior):
    """
    Ordena 'lista' do maior para o menor, caso 'maior' seja True; caso
    contrário, ordena do menor para o maior. Essa função modifica a lista
    passada por parâmetro.

    Parâmetros: lista de números ou strings e um booleano.
    Retorna: nada.
    """
    if maior == True:
        lista.sort(reverse = True)
    else:
        lista.sort(reverse = False)

def moda(lista):
    """
    Encontra a moda de 'lista', isto é, o valor que mais se repete; em caso de
    empate, retorne o que aparece primeiro.

    Parâmetros: lista de strings.
    Retorna: a moda de 'lista'.
    """
    lista_repeticao = [0 for _ in range(len(lista))]

    for i in lista:
        for n in range(len(lista)):
            if lista[n] == i:
                lista_repeticao[n] += 1

    indice_moda = 0
    for i in range(len(lista_repeticao)):
        if lista_repeticao[i]>lista_repeticao[indice_moda]:
            indice_moda = i

    moda = lista[indice_moda]
    return moda
        


def mediana(valores):
    """
    Encontra a mediana de 'valores', isto é, o valor que ocupa a posição
    central da lista ordenada. Quando a lista tem tamanho par,
    definimos a mediana como o valor da primeira posição na segunda
    metada da lista ordenada.

    Parâmetros: lista de floats.
    Retorna: a mediana de 'valores'.
    """

    maior = False
    ordena(valores,maior)

    if len(valores)%2 == 0:
        indice = (len(valores)//2)
    else:
        indice = (len(valores)-1)//2

    mediana = valores[indice]
    return mediana

def media(valores):
    """
    Encontra a média de 'valores'.

    Parâmetros: lista de floats.
    Retorna: a média de 'valores'.
    """
    soma = 0
    num_elementos = len(valores)
    for elemento in valores:
        soma+=elemento
    media = soma/num_elementos
    return media
    
def media_ponderada(valores, pesos):
    """
    Encontra a média ponderada de 'valores'.

    Parâmetros: listas de floats.
    Retorna: a média ponderada de 'valores'.
    """
    soma_valores = 0
    soma_pesos = 0
    for i in range(len(valores)):
        soma_valores += (pesos[i]*valores[i])
        soma_pesos += pesos[i]

    media_ponderada = soma_valores / soma_pesos
    return media_ponderada



def filtrar_entre(valores, menor, maior):
    """
    Cria uma lista com os números de 'valores' que estejam no intervalo
    ['menor', 'maior') (o primeiro intervalo é fechado e o segundo é aberto).

    Parâmetros: lista de floats e os limites.
    Retorna: a lista filtrada.
    """
    lista_filtrada = []
    for elemento in valores:
        if (elemento >= menor and elemento < maior):
            lista_filtrada.append(elemento)

    return lista_filtrada



def filtrar_caracteristica(lista, caracteristica, alvo):
    """
    Cria uma lista com os elementos de 'lista' cuja posição em 'caracteristica'
    seja igual a 'alvo'. Por exemplo, com a entrada abaixo, retornaríamos
    ['Alemanha', 'Portugal']:
    lista = ['Brasil', 'Alemanha', 'Angola', 'Portugal']
    caracteristica = ['América do Sul', 'Europa', 'África', 'Europa']
    alvo = 'Europa'

    Parâmetros: listas de números ou strings e um valor alvo.
    Retorna: a lista com a característica filtrada.
    """
    lista_c_filtrada = []
    for i in range(len(caracteristica)):
        if caracteristica[i]==alvo:
            lista_c_filtrada.append(lista[i])
    
    return lista_c_filtrada

def histograma(valores, intervalos):
    """
    Cria uma lista com as frequências do histograma de 'valores', divididas nas
    classes conforme a lista 'intervalos'. Por exemplo, se temos [10, 20, 30]
    como intervalos, devemos obter as frequências dos intervalos [10, 20) e [20,
    30).

    Parâmetros: listas de números.
    Retorna: lista de frequência do histograma.
    """
    num_intervalos = len(intervalos)-1
    frequencia_histograma = [0 for _ in range(num_intervalos)]
    
    for i in range(num_intervalos):
        min = intervalos[i]
        max = intervalos[i+1]
        for elemento in valores:
            if (elemento >= min and elemento < max):
                frequencia_histograma[i]+=1

    return frequencia_histograma

def maiores_k(valores, k):
    """
    Cria uma lista com os 'k' maiores números de 'valores'.

    Parâmetros: lista de inteiros e um número inteiro.
    Retorna: lista com os 'k' maiores números.
    """
    maior = True
    ordena(valores,maior)
    lista_maiores_k = valores[:k]
    return lista_maiores_k


def menores_k(valores, k):
    """
    Cria uma lista com os 'k' menores números de 'valores'.

    Parâmetros: lista de inteiros e um número inteiro.
    Retorna: lista com os 'k'menores números.
    """
    maior = False
    ordena(valores,maior)
    lista_maiores_k = valores[:k]
    return lista_maiores_k


def remove_duplicatas(lista):
    """
    Cria uma lista removendo todos os elementos duplicados de 'lista', mantendo
    a ordem relativa original. Use somente listas, for/while e variáveis
    simples para implementar essa função.

    Parâmetros: listas de strings.
    Retorna: 'lista' sem duplicatas.
    """

    lista_remove_duplicatas = []
    
    for i in range(len(lista)):
        if lista[i] not in lista_remove_duplicatas:
            lista_remove_duplicatas.append(lista[i])
                
    return lista_remove_duplicatas

