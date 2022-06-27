def mostra_saldo(saldo):
    """
    Dado 'saldo', se 'saldo' for None, devolve "Esta conta não existe"
    Do contrário, devolve o valor de 'saldo' formatado para 2 casas decimais
    """
    if saldo == None:
        print("Esta conta não existe")
    else:
        print("O saldo da conta é R$ " + format(saldo, '.2f'))

def mostra_extrato(mensagem_erro,extrato):
    """
    Dada 'mensagem_erro' e 'extrato', se 'mensagem_erro' for None, imprime todas as linhas de 'extrato'.
    Do contrário, imprime 'mensagem_erro'.
    """
    if mensagem_erro == None:
        for linha in extrato:
            print(linha)
    else:
        print(mensagem_erro)

def le_varios_dados():
    """
    Retorna a função de leitura de diferentes variáveis separadas por espaço, representando a leitura de vários dados.
    """
    return input().split()

def le_dado():
    """
    Retorna a função de leitura, representando a leitura de um dado.
    """
    return input()

def mostra(mensagem):
    """
    Retorna a função print(), imprimindo 'mensagem'.
    """
    return print(mensagem)

def le_dados_movimentacao():
    """
    Lê a entrada do teclado e guarda as informações nas variáveis 'dados_entrada', 'num_conta', 'valor', 'data', 'descricao'.
    Retorna: variáveis num_conta (inteiro), valor (float), data (string), descricao (string)
    """
    dados_entrada = list(map(str, input().split()))
    num_conta = dados_entrada[0]
    valor = float(dados_entrada[1])
    data = dados_entrada[2]
    descricao = ' '.join(map(str, dados_entrada[3:]))
    return num_conta,valor,data,descricao