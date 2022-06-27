
def sequencia_pedrinho(numero):
    """
    Dado um número 'numero', retorna o valor de Pnumero na sequência de pedrinho
    """ 
    valores_pedrinho = {}
    valores_pedrinho = calcula_p(numero, valores_pedrinho) 
    return valores_pedrinho[numero]


def calcula_p(numero, valores_pedrinho):
    """
    Dado um número 'numero' e um dicionário 'valores_pedrinho', calcula o valor de P'numero' na sequência de Pedrinho e
    retorna o dicionário com os valores de Pedrinho atualizados.
    """
    if numero not in valores_pedrinho:

        if numero <=3:

            valores_pedrinho[numero] = numero

        else:

            pn_1 = calcula_p(numero-1, valores_pedrinho)[numero-1]
            pn_2 = calcula_p(numero-2, valores_pedrinho)[numero-2]
            pn_3 = calcula_p(numero-3, valores_pedrinho)[numero-3]

            valores_pedrinho[numero] = pn_1 + 2*pn_2 + 3*pn_3

    return valores_pedrinho

def main():

    numero = int(input())
    Pnum = sequencia_pedrinho(numero)
    print(Pnum)

main()


