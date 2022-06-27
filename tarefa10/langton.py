def le_tabuleiro(numero_linhas):
    """
    Lê os elementos de 'numero_linhas' linhas do usuário e os guarda na matriz 'tabuleiro'.
    Retorna: matriz 'tabuleiro'
    """
    tabuleiro = []
    for _ in range(numero_linhas):
        linha = input()
        tabuleiro.append([elemento for elemento in linha])
    return tabuleiro

def le_dados():
    """
    Retorna a funcao de leitura para ler vários inteiros separados por " ".
    """
    return map(int, input().split())


def calcula_nova_direcao(tabuleiro, x, y, direcao_atual):
    """
    Se o elemento do tabuleiro for preto ("#"), calcula a nova direção rotacionando 90° para a esquerda. Do contrário, se for branco
    ("."), calcula a nova direção rotacionando 90° para a direita.
    Retorna: nova_direcao
    """
    preto = "#"
    branco = "."

    if tabuleiro[x][y] == preto:
        if direcao_atual == "cima":
            nova_direcao = "esquerda"
        elif direcao_atual == "direita":
            nova_direcao = "cima"
        elif direcao_atual == "baixo":
            nova_direcao = "direita"
        elif direcao_atual == "esquerda":
            nova_direcao = "baixo"

    else:
        if direcao_atual == "cima":
            nova_direcao = "direita"
        elif direcao_atual == "direita":
            nova_direcao = "baixo"
        elif direcao_atual == "baixo":
            nova_direcao = "esquerda"
        elif direcao_atual == "esquerda":
            nova_direcao = "cima"

    return nova_direcao
    
def calcula_nova_posicao(x, y, nova_direcao):
    """
    Dada 'nova_direcao', calcula a nova posicao da formiga ao andar um passo, ou seja, as coordenadas x e y.
    Retorna: x e y
    """

    if nova_direcao == "baixo":
        y += 1

    elif nova_direcao == "cima":
        y -= 1
        
    elif nova_direcao == "direita":
        x -= 1

    elif nova_direcao == "esquerda":
        x += 1

    return x, y

def inverte_cor(tabuleiro, x, y):
    """
    Se o valor do elemento do tabuleiro for preto ("#"), muda para branco ("."). Do contrário, se for branco ("."), muda para preto ("#").
    Retorna: lista 'tabuleiro' com o valor atualizado.
    """
    preto = "#"
    branco = "."

    if tabuleiro[x][y] == preto:
        tabuleiro[x][y] = branco
    else:
        tabuleiro[x][y] = preto
    
    return tabuleiro

def mostra_tabuleiro(tabuleiro):
    """
    Imprime os elementos da matriz 'tabuleiro', sem espaço, linha após linha.
    """
    for linha in tabuleiro:
        for elemento in linha:
            print(elemento, end="")
        print()

def move_formiga(num_interacoes, num_colunas, numero_linhas, tabuleiro, contador_passos = "", x = "", y = "", nova_direcao = ""):
    """
    Modifica o tabuleiro de acordo com 'num_interacoes' e imprime o tabuleiro com os quadrados atualizados.
    """
    
    if contador_passos == "":

        contador_passos = 0
        x = num_colunas // 2
        y = numero_linhas // 2
        nova_direcao = "baixo"

    if contador_passos < num_interacoes:

        if (0 <= x) and (x < num_colunas) and (0 <= y) and (y < numero_linhas):

            contador_passos += 1
            tabuleiro = inverte_cor(tabuleiro, y, x)
            nova_direcao = calcula_nova_direcao(tabuleiro, y, x, nova_direcao)
            x, y = calcula_nova_posicao(x, y, nova_direcao)

        return move_formiga(num_interacoes, num_colunas, numero_linhas, tabuleiro, contador_passos, x, y, nova_direcao)

    else:
        mostra_tabuleiro(tabuleiro)

def main():

    num_interacoes, numero_linhas, num_colunas = le_dados()
    tabuleiro = le_tabuleiro(numero_linhas)
    move_formiga(num_interacoes, num_colunas, numero_linhas, tabuleiro)


main()
