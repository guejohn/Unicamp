import math

def interpolar(lista,Nmin):
    """
    Dada uma lista 'lista' e um inteiro 'Nmin', retorna uma lista com a média aritmética dos elementos da lista
    cujos índices estão em um intervalo [d*j, (d*j)+d)), sendo 'd' e 'j' variáveis a serem definidas posteriormente na função.

    Parâmetros: uma lista de listas e um inteiro
    Retorna: uma lista
    """
    
    lista_interpolada = []

    for i in range(len(lista)):
        lista_elemento = []
        ni = len(lista[i])
        d = ni/Nmin
        for j in range(Nmin):
            soma=0
            cont=0
            for indice in range(math.ceil(d*j),math.ceil((d*j)+d)):
                if indice in range(len(lista[i])):
                    soma += float(lista[i][indice])
                    cont+=1

            media = calcula_media_simples(soma,cont)
            lista_elemento.append(media)
        lista_interpolada.append(lista_elemento)
   
    lista_interpolada = calcula_media_colunas(lista_interpolada)
    
    return lista_interpolada

        
def reamostrar(lista,Nmin):
    """
    Comprime todos os sinais - ou seja, as listas da lista 'lista' - para que tenham a frequência do sinal com menor frequência
    e retorna uma lista com as médias aritméticas dos sinais comprimidos

    Parâmetros: uma lista de floats e um inteiro
    Retorna: lista de floats
    """
    frequencias_iguais = verifica_tamanho_listas(lista)

    if frequencias_iguais:
        lista_medias = calcula_media_colunas(lista)

    else:
        lista_medias = interpolar(lista,Nmin)
    
    return lista_medias


def calcula_media_simples(valor,num_elementos):
    """
    Dado um valor 'valor' e um número de elementos 'num_elementos', calcula e retorna a respectiva média aritmética.

    Parâmetros: um float e um inteiro
    Retorna: um float

    """
    media = valor/num_elementos
    return media


def verifica_tamanho_listas(lista):
    """
    Dada uma lista de listas 'lista', verifica se o tamanho
    de todas as listas dentro de 'lista' é o mesmo

    Parâmetros: uma lista de listas
    Retorna: um booleano
    """
    todos_iguais = True
    igual = [len(lista[i]) == len(lista[0]) for i in range(len(lista))]
    if False in igual:
        todos_iguais = False

    return todos_iguais

def calcula_media_colunas(lista):
    """
    Dada uma lista de listas 'lista', calcula a média de cada coluna dos elementos de 'lista'
    e adiciona as médias à uma lista 'lista_médias'
    
    Parâmetros: uma lista de listas de floats
    Retorna: lista de floats das médias
    """
    lista_medias = []
    soma = [0 for i in range(len(lista[0]))]

    for i in range(len(lista[0])):
        for n in range(len(lista)):
            soma[i] += float(lista[n][i])

        media = soma[i]/len(lista)
        lista_medias.append(format(media,".2f"))

    return lista_medias


def calcular_menor_frequencia(lista):
    """
    Dada uma lista de frequências 'lista', percorre cada lista dentro de 'lista' e retorna o número de elementos da menor lista

    Parâmetros: uma lista de listas
    Retorna: um número inteiro
    """
    
    menor = len(lista[0])
    for i in lista:
        if len(i) < menor:
            menor = len(i)
    return menor

def imprimir(lista):
    """
    Dada uma lista 'lista', imprime todos os elementos da lista em uma mesma linha

    Parâmetros: uma lista
    Retorna: nada
    """
    for elemento in lista:
        print(elemento, end=" ")

def ler_sinais():
    """
    Dado um número inteiro 'm', que será recebido na função, lê a entrada do input 'm' vezes e adiciona as entradas em uma
    lista 'lista_sinais'

    Parâmetros: número inteiro 'm'
    Retorna: lista de números
    """

    lista_sinais = []

    m = int(input())
    for i in range(m):
        sinal = input().split()
        lista_sinais.append(sinal)
    return lista_sinais

def verifica_lista_vazia(lista):
    """
    Verifica se alguma lista dentro da lista de listas 'lista' está vazia.

    Parâmetros: uma lista de listas
    Retorna: um booleano
    """
    tem_vazio = False
    for i in lista:
        if len(i)==0:
            tem_vazio = True

    return tem_vazio

def main():
    
    lista_sinais = ler_sinais()
    tem_vazio = verifica_lista_vazia(lista_sinais)
    if tem_vazio == False:
        Nmin = calcular_menor_frequencia(lista_sinais)
        lista_reamostrada = reamostrar(lista_sinais,Nmin)
        imprimir(lista_reamostrada)
        
main()