def inicializa_lista():
    """
    Retorna '[]', representando a inicialização de uma lista
    """
    return []
    
def inicializa_dicionario():
    """
    Retorna 'dict()', representando a inicialização de um dicionário
    """
    return dict()

def le_numero():
    """
    Lê e retorna um número inteiro

    Parâmetros: nenhum
    Retorna: inteiro 'numero'
    """
    numero = int(input())
    return numero

def le_moleculas(m,tipo_moleculas):
    """
    Lê um par de moléculas 'm' vezes e adiciona os dois números de cada par lido no dicionário 'tipo_moleculas', sendo o segundo número do par adicionado à
    lista de moléculas pareáveis do primeiro e vice-versa.

    Parâmetros: inteiro 'm' e um dicionário 'tipo_moleculas'
    Retorna: dicionário atualizado 'tipo_moleculas'
    """
    for _ in range(m):

        num1, num2 = input().split()
        
        if num1 in tipo_moleculas:
            tipo_moleculas[num1].add(num2)   
        else:
            tipo_moleculas[num1] = {num2}

        if num2 in tipo_moleculas:
            tipo_moleculas[num2].add(num1)
            
        else:
            tipo_moleculas[num2] = {num1}
 
    return tipo_moleculas


def verifica_cadeias_fortes(tipo_moleculas):
    """
    Dado 'tipos_moleculas', verifica quais moléculas formam cadeias fortes - isto é, um trio de moléculas em que todas podem ser ligadas entre si, par a par.
    Parâmetros: dicionário 'tipo_moleculas'
    Retorna: lista 'cadeias_fortes', com as cadeias fortes em ordem lexicográfica.
    """

    chave_cadeias_fortes = inicializa_dicionario()
    cadeias_fortes = inicializa_lista()

    for numero_molecula, conjunto_moleculas_pareaveis in tipo_moleculas.items():

        for j, valor in enumerate(conjunto_moleculas_pareaveis):

            if len(conjunto_moleculas_pareaveis)-j>1:

                for n, valor2 in enumerate(conjunto_moleculas_pareaveis):

                    if valor != valor2:
                    
                        if valor in tipo_moleculas[valor2]:

                            trio = sorted([int(numero_molecula), int(valor), int(valor2)])
                            chave_trio = ' '.join(map(str, trio))

                            if chave_trio not in chave_cadeias_fortes:
                                chave_cadeias_fortes[chave_trio] = True
                                cadeias_fortes.append(trio)

                tipo_moleculas[valor].remove(numero_molecula)
                    
    cadeias_fortes.sort()
    return cadeias_fortes

def mostra_itens(dicionario):
    """
    Imprime as listas do dicionário 'dicionário', uma por linha, com os elementos de cada lista separados por espaço.
    """
    for molecula in dicionario:
        molecula = ' '.join(map(str, molecula))
        print(molecula)   
    
def main():

    m = le_numero()
    tipo_moleculas = inicializa_dicionario()
    tipo_moleculas = le_moleculas(m,tipo_moleculas)
    cadeias_fortes = verifica_cadeias_fortes(tipo_moleculas)
    
    mostra_itens(cadeias_fortes)     
       
main()
