import sys
from modulo_analise import ordena, filtrar_caracteristica, histograma

def produtividade(anos):
    """
    Informe a quantidade de filmes lançados em cada ano, da lista 'anos', desde 'inicio' até 'fim' (que serão digitados)

    Parâmetros: 1 lista 'anos'
    Retorna: os anos filtrados e o respectivo número de vezes que aparecem na lista.
             Exemplo:
             1990: 11
             1991: 12
             ...
    """
    inicio,fim = list(map(int, input().split()))
    maior = False
    lista_anos = ordena(anos,maior)
    lista_frequencia = frequencia(inicio, fim, anos)
    cont = 0
    for ano in range(inicio,fim+1):
        print(f"{ano}: {lista_frequencia[cont]}")
        cont+=1

def anos_presentes(anos):
    """
    Informa, em ordem crescente, os anos, da lista 'anos', em que foram lançados filmes, desde 'inicio' até 'fim' (que serão digitados).

    Parâmetros: lista 'anos'
    Retorna: os anos dos filmes filtrados
            Exemplo:
            1990
            1991
            ...
    """
    inicio, fim = list(map(int, input().split()))
    maior = False
    ordena(anos,maior)
    lista_anos = filtrar_intervalo_fechado(anos,inicio,fim+1)
    for ano in lista_anos:
        print(ano)

def filmes_por_classificacao(indices,classificacoes):
    """
    Dada uma string classificacao - que será digitada - informa, em ordem crescente,
    os identificadores dos filmes na lista 'indices' com a classificação indicativa 'classificacao', na lista 'classificacoes'

    Parâmetros: 2 listas ('indices' e 'classificacoes')
    Retorna: os identificadores filtrados
            Exemplo: 
            476
            954
            ...    
    """
    classificacao = input()
    lista_indices = filtrar_caracteristica(indices,classificacoes, classificacao)
    maior = False
    ordena(lista_indices,maior)
    for elemento in lista_indices:
        print(elemento)

def histograma_dos_anos(anos):
    """
    Dada uma lista intervalos - que será digitada - informa o histograma dos anos de lançamento dos filmes, da lista 'anos',
    considerando os intervalos formados por números seguidos [intervalos[i], intervalos[i+1]), onde o primeiro 
    intervalo é fechado e o segundo aberto

    Parâmetros: lista 'anos'
    Retorna: os intervalos e as respectivas frequências dos histogramas filtrados
             Exempĺo:
             [2000, 2005): 146
             [2005, 2008): 147
    """
    intervalos = list(map(int, input().split()))
    lista_histogramas = histograma(anos,intervalos)
    for i in range(len(intervalos)-1):
        print(f"[{intervalos[i]}, {intervalos[i+1]}): {lista_histogramas[i]}")

def filmes_por_pais_e_classificacao(indices,paises,classificacoes):
    """
    Dadas strings 'pais' e 'classificacao' - que serão digitadas - informa, em ordem crescente,
    os identificadores da lista 'indices', dos filmes lançados no país 'pais' da lista 'paises', e que possuem classificação
    indicativa 'classificacao' na lista 'classificacoes'
    
    Parâmetros: listas 'indices', 'paises', 'classificacoes'
    Retorna: identificadores filtrados
            Exemplo: 
            7932
    """
    pais, classificacao = input().split()
    lista_indices = filtrar_duas_caracteristicas(indices,paises,classificacoes,pais,classificacao)
    maior = False
    ordena(lista_indices,maior)
    for elemento in lista_indices:
        print(elemento)

def filtrar_duas_caracteristicas(lista, caracteristica1, caracteristica2, alvo1, alvo2):
    """
    Cria uma lista com os elementos de 'lista' cuja posição em 'caracteristica1'
    é igual a 'alvo1' e posição em 'caracteristica2' é igual a 'alvo2'. 
    
    Parâmetros: 3 listas e 2 valores alvo.
    Retorna: lista com as características filtradas.
    """
    lista_c_filtrada = []
    for i in range(len(caracteristica1)):
        if caracteristica1[i] == alvo1 and caracteristica2[i] == alvo2:
            lista_c_filtrada.append(lista[i])
    return lista_c_filtrada

def filtrar_intervalo_fechado(valores, menor, maior):
    """
    Cria uma lista com os 'valores' que estejam no intervalo
    ['menor', 'maior'] (ambos os extremos para intervalo *FECHADO*). Cada elemento é contado uma única vez, ainda que apareça
    mais vezes na lista.

    Parâmetros: lista de elementos, menor valor do intervalo e maior valor do intervalo
    Retorna: lista filtrada.
    """

    lista_filtrada = []
    for elemento in valores:
        if (elemento >= menor and elemento < maior):
            if elemento not in lista_filtrada:
                lista_filtrada.append(elemento)

    return lista_filtrada


def frequencia(inicio,fim,lista):
    """
    Calcula, dentro de uma lista recebida 'lista', o número de vezes que cada elemento aparece na lista, no intervalo fechado
    ['inicio','fim'] da lista.

    Parâmetros: valor inicial do intervalo, valor final do intervalo e uma lista (dos elementos a serem filtrados).
    Retorna: uma lista com a frequência de cada elemento, ordenada seguindo a ordem da respectiva frequência de 'inicio' até
    a respectiva frequência de 'fim'.
    """
    lista_frequencia = []
    for i in range(inicio,fim+1):
        frequencia = 0
        for elemento in lista:
            if elemento == i:
                frequencia+=1
        lista_frequencia.append(frequencia)

    return lista_frequencia


def ler_dados_filmes(caminho):
    """
    Lê os dados de um arquivo de filmes localizado em 'caminho' e divide as informações de cada coluna (indice, pais, ano, classificação e duração) em
    respectivas listas.

    Parâmetros: o caminho do local onde o arquivo de filmes se encontra
    Retorna: 5 listas relativas as informações listadas acima (indice, pais, ano, classificação e duração)

    """
    indices = []
    paises = []
    anos = []
    classificacoes = []
    duracoes = []
    with open(caminho) as f:
        for linha in f:
            indice, pais, ano, classe, duracao = linha.split()
            indices.append(int(indice))
            paises.append(pais)
            anos.append(int(ano))
            classificacoes.append(classe)
            duracoes.append(int(duracao))

    return(indices,paises,anos,classificacoes,duracoes)

def main():

    caminho = 'testes/filmes.dat'
    indices,paises,anos,classificacoes,duracoes = ler_dados_filmes(caminho)

    acao = sys.argv[1]
    
    if acao == 'produtividade':
        produtividade(anos)
    
    elif acao == 'anos_presentes':
        anos_presentes(anos)

    elif acao == 'filmes_por_classificacao':
        filmes_por_classificacao(indices,classificacoes)

    elif acao == 'histograma_dos_anos':
        histograma_dos_anos(anos)

    elif acao == 'filmes_por_pais_e_classificacao':
        filmes_por_pais_e_classificacao(indices,paises,classificacoes)

main()