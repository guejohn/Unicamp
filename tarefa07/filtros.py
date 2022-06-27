import sys
from bordas import le_imagem, criar_arquivo

def bordas(imagem):
    """
    Dada uma matriz 'imagem', cria uma nova matriz 'imagem_borda', com a convolução de cada elemento da lista
    (que representam pixels), através de um kernel.

    Parâmetros: uma matriz de inteiros 'imagem'
    Retorna: uma matriz de strings 'imagem_borda'
    """
    kernel = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]

    imagem_borda = [ [ "0 " for j in range(len(imagem[0]))] for i in range(len(imagem)) ]

    for i in range(1,len(imagem)-1):

        for j in range(3,len(imagem[0])-3,3):
            
            imagem_borda[i][j] = convolucao(imagem, kernel, i, j)
            imagem_borda[i][j+1] = convolucao(imagem, kernel, i, j+1)
            imagem_borda[i][j+2] = convolucao(imagem, kernel, i, j+2)
                       
    return imagem_borda

def convolucao(imagem, kernel, i, j):
    """
    Dada uma matriz 'imagem', uma lista 'kernel', e dois inteiros 'i' e 'j', calcula a convolução
    do elemento[i][j].
    No processo de convolução, somam-se os valores dos elementos da lista 'imagem' em volta do elemento[i][j], multiplicados pelo valor
    daquela posição no kernel, considerando os valores máximo e mínimo como 255 e 0.

    Parâmetros: uma matriz 'imagem', uma matriz 3x3 'kernel' e dois inteiros 'i' e 'j'
    Retorna: uma string
    """

    pixel = (imagem[i][j]*kernel[1][1]) + (imagem[i-1][j-3]*kernel[0][0]) + (imagem[i-1][j]*kernel[0][1]) + (imagem[i-1][j+3]*kernel[0][2]) + (imagem[i][j+3]*kernel[1][2]) + (imagem[i+1][j+3]*kernel[2][2]) + (imagem[i+1][j]*kernel[2][1]) + (imagem[i+1][j-3]*kernel[2][0]) + (imagem[i][j-3]*kernel[1][0])
    
    if pixel<0:
        pixel = 0

    elif pixel>255:
        pixel=255

    return str(pixel)+" "

def main():
    nome_filtro = sys.argv[1]
    nome_arquivo =  sys.argv[2]
    nome_arquivo_bordas = sys.argv[3]
    tipo_arquivo, largura, altura, imagem = le_imagem(nome_arquivo)
    imagem_borda = bordas(imagem)
    criar_arquivo(nome_arquivo_bordas, tipo_arquivo, largura, altura, imagem_borda)

if __name__ == "__main__":
    main()