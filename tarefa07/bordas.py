import sys
    
def criar_arquivo(nome_arquivo, tipo_arquivo, largura, altura, matriz):
    """
    Cria um novo arquivo de nome 'nome_arquivo' contendo o 'tipo_arquivo', 'largura', 'altura' e
    os elementos da 'matriz', uma em cada linha (estando somente a largura e altura na mesma linha).

    Parâmetros: 4 strings (nome_arquivo, tipo_arquivo, largura, altura) e uma matriz
    Retorna: nada

    """
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(tipo_arquivo + '\n')
        arquivo.write(largura + " ")
        arquivo.write(altura + '\n')
        if tipo_arquivo == "P3":
            arquivo.write('255' + '\n')
        
        for i in range(int(len(matriz))):
            for j in range(int(len(matriz[0]))):
                linha = str(matriz[i][j]) + '\n'
                arquivo.write(linha.strip("\n"))
            arquivo.write("\n")


def bordas_pbm(imagem):
    """
    Dada uma matriz 'imagem', com elementos iguais a 0 ou 1, gera uma nova matriz, substituindo os elementos da borda da matriz
    original, isto é, os elementos que têm ao menos um vizinho que não está no objeto (ou seja, um vizinho de valor 0) por 1 e os demais por 0.
    Considera-se "vizinho" os 8 elementos ao redor do elemento central (cantos esquerdo, direito, superior, inferior, superior esquerdo,
    superior direito, inferior esquerdo e inferior direito do elemento)

    Parâmetros: matriz de inteiros 'imagem'
    Retorna: matriz de strings 'imagem_borda'
    """
    imagem_borda = [ [ "0 " for j in range(len(imagem[0]))] for i in range(len(imagem)) ]

    for i in range(1,len(imagem)-1):

        for j in range(1,len(imagem[0])-1):

            borda_detectada = (imagem[i][j]==1) and ((imagem[i-1][j-1] == 0) or (imagem[i-1][j] == 0) or (imagem[i-1][j+1] == 0) or (imagem[i][j+1] == 0) or (imagem[i+1][j+1] == 0) or (imagem[i+1][j] == 0) or (imagem[i+1][j-1] == 0) or (imagem[i][j-1] == 0))
            
            if borda_detectada:
                imagem_borda[i][j] = "1 "
                
    return imagem_borda

def le_imagem(nome_arquivo):
    """
    Dado o nome de um arquivo 'nome_arquivo', abre o respectivo arquivo, lê as informações de todas as linhas do arquivo, uma por vez,
    e as guarda em variáveis e em uma matriz.

    Parâmetros: uma string
    Retorna: 3 strings e uma matriz de inteiros 'imagem'
    """
    linhas = []
    imagem = []
    
    with open(nome_arquivo) as arquivo:
        tipo_arquivo = arquivo.readline().strip()
        largura, altura = arquivo.readline().split()
        if tipo_arquivo == "P3":
            valor_maximo = arquivo.readline()

        for linha in arquivo:
            linhas = []

            linhas.append(list(map(int, linha.split())))
            for i in linhas:
                imagem.append(i)

    return tipo_arquivo,largura,altura,imagem
    


def main():
    nome_arquivo =  sys.argv[1]
    nome_arquivo_bordas = sys.argv[2]
    tipo_arquivo, largura, altura, imagem = le_imagem(nome_arquivo)
    imagem_borda = bordas_pbm(imagem)
    criar_arquivo(nome_arquivo_bordas, tipo_arquivo, largura, altura,imagem_borda)
    
if __name__ == "__main__":
    main()

