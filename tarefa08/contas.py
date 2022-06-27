def inicializa_contas():
    """
    Devolve um objeto representando o conjunto
    de contas bancárias inicialmente vazio.
    """
    return []

def inicializa_movimentacoes():
    """
    Devolve um objeto representando o conjunto
    de movimentacoes inicialmente vazio.
    """
    return []

def verifica_conta_aberta(num_conta,contas):
    """
    Verifica se a conta 'num_conta' existe em 'contas'
    Devolve: 
            - True se a conta já existe
            - False se a conta não existe
    """

    for conta in contas:
        if conta['numero'] == num_conta:
            return True

    return False


def adiciona_conta(num_conta, contas):
    """
    Cria uma nova conta identificada por 'num_conta' com
    saldo 0.0 e adiciona à 'contas', se 'num_conta' não existir em 'contas'.
    Devolve: lista 'contas' e uma mensagem:
            - "Conta aberta com sucesso" se a conta não existia e foi adicionada
            - "Número de conta já existe" se a conta já existia anteriormente
        
    """
    conta_aberta = verifica_conta_aberta(num_conta,contas)

    if conta_aberta == False:
        nova_conta = {
        "numero": num_conta,
        "saldo": 0.0
        }
        contas.append(nova_conta)
        mensagem = "Conta aberta com sucesso"

    else:
        mensagem = "Número de conta já existe"

    return contas, mensagem


def movimenta(tipo, num_conta, valor, data, descricao, movimentacoes, contas):
    """
    Dados 'tipo', 'num_conta', 'valor', 'data', 'descricao', lista 'movimentacoes' e lista 'contas' da movimentação,
    verifica se a operação pode ser efetuada, isto é, se a data da movimentação não for retroativa e a conta existir. 
    Se puder, realiza uma movimentação de número 'num_conta' e tipo 'tipo' na conta 'numero_conta' de valor 'valor' no dia 'data' descrita por 'descricao'.

    Devolve: lista 'movimentacoes' e lista 'contas' e a mensagem:
            - "{Tipo} realizado com sucesso", se a movimentação puder ser efetuada
            - "Movimentação tem data retroativa", se a data da movimentação for retroativa em relação à última movimentação da mesma conta
            - "Esta conta não existe", se 'num_conta' não existir em 'contas'
    """
    conta_existe = verifica_conta_aberta(num_conta,contas)

    if conta_existe == True:
        
        saldo_atual = consulta_saldo(num_conta,contas)
        saldo_apos = float(saldo_atual) + float(valor)
        nova_movimentacao = cria_nova_movimentacao(num_conta, tipo, valor, data, descricao,saldo_apos)

        if encontra_movimentacao_anterior(num_conta,movimentacoes):
            
            data_ultima_mov = encontra_ultima_data(num_conta,movimentacoes)

            if data_nao_retroativa(data,data_ultima_mov):
                contas = altera_saldo(contas, num_conta, valor)
                movimentacoes.append(nova_movimentacao)
                return contas, tipo + " realizado com sucesso", movimentacoes

            else:
                return contas,"Movimentação tem data retroativa", movimentacoes

        else:
            contas = altera_saldo(contas, num_conta, valor)
            movimentacoes.append(nova_movimentacao)
            return contas, tipo + " realizado com sucesso", movimentacoes

    else:
        return contas,"Esta conta não existe", movimentacoes


def consulta_saldo(num_conta,contas):
    """
    Devolve o saldo da conta identificada por 'num_conta' em 'contas. 
    Se a conta não existir, devolve None.
    """
    conta_aberta = verifica_conta_aberta(num_conta,contas)
    
    if conta_aberta:
        for conta in contas:
            if conta["numero"] == num_conta:
                saldo = conta["saldo"]
    else:
        saldo = None

    return saldo

def data_nao_retroativa(data1,data2):
    """
    Dadas duas datas 'data1' e 'data2', verifica se a 'data1' é posterior ou idêntica à 'data2'.
    Se for, devolve True. Do contrário, se for anterior à 'data2', devolve False.
    """
    dia1, mes1, ano1 = map(int, data1.split('/'))
    dia2, mes2, ano2 = map(int, data2.split('/'))
    
    if (ano1>ano2) or (ano1==ano2 and mes1>mes2) or (ano1==ano2 and mes1==mes2 and dia1>=dia2):
        return True
    else:
        return False

def altera_saldo(contas, num_conta, valor):
    """
    Altera o saldo da conta identificada por 'num_conta' em 'contas', somando 'valor' ao saldo atual da conta.
    Devolve: lista 'contas' com saldo de 'num_conta' atualizado.
    """
    for conta in contas:
        if conta["numero"] == num_conta:
            conta["saldo"] += float(valor)

    return contas

def gera_extrato(num_conta, data, movimentacoes, contas):
    """
    Dada uma conta identificada por 'num_conta' em 'contas', gera uma lista com as movimentações da conta a partir da data 'data' (incluindo 'data').
    Devolve:
        - lista 'extrato' com as movimentações que satisfazem as condições acima e uma mensagem de erro None, se a conta 'num_conta' existir
        - lista 'extrato' vazia e a mensagem de erro "Esta conta não existe", se a conta identificada por 'num_conta' não existir
    """
    extrato = []

    if verifica_conta_aberta(num_conta,contas):
        for movimentacao in movimentacoes:
            if movimentacao["numero_conta"] == num_conta:
                if data_nao_retroativa(movimentacao["data"], data):
                    linha = movimentacao["tipo"]+' de valor R$ '+ format(movimentacao["valor"], '.2f') +' realizado em '+ movimentacao["data"] + '\n'+ 'Descrição adicional: ' + movimentacao["descricao"] + '\n' + 'Saldo após movimentação: R$ '+ str(movimentacao["saldo_apos"])
                    extrato.append(linha)
        mensagem_erro = None
    else:
        mensagem_erro = "Esta conta não existe"
        
    return extrato, mensagem_erro

def fecha_conta(num_conta, contas):
    """
    Dada uma conta identificada por 'num_conta' em 'contas', exclui a conta de 'contas', se ela existir e o seu saldo for igual a 0.
    Devolve: lista 'contas' e a mensagem:
            - "Conta fechada com sucesso", se a conta existir e o seu saldo for igual a 0
            - "A conta não pode ser fechada", se a conta existir mas o seu saldo for diferente de 0
            - "Esta conta não existe", se a conta não existir
    """
    conta_aberta = verifica_conta_aberta(num_conta,contas)
    
    if conta_aberta:
        saldo = consulta_saldo(num_conta,contas)

        if float(saldo) == 0.0:
            for i, conta in enumerate(contas):
                if conta["numero"] == num_conta:
                    contas.pop(i)
            mensagem = "Conta fechada com sucesso"
        else:
            mensagem = "A conta não pode ser fechada"
    else:
        mensagem = "Esta conta não existe"
    
    return mensagem, contas

def encontra_movimentacao_anterior(num_conta,movimentacoes):
    """
    Verifica se há alguma movimentação em 'movimentacoes' com o número de conta 'num_conta'.
    Devolve:
        - True, se existir
        - False, se não existir
    """
    for movimentacao in movimentacoes:
        if movimentacao["numero_conta"] == num_conta:
            return True
    return False

def cria_nova_movimentacao(num_conta, tipo, valor, data, descricao,saldo_apos):
    """
    Cria uma nova movimentação (um dicionário), contendo os dados 'num_conta', 'tipo', 'valor', 'data', 'descricao' e 'saldo_apos'.
    Devolve: a nova movimentação.
    """
    nova_movimentacao = {
                        "numero_conta": num_conta,
                        "tipo": tipo,
                        "valor": abs(float(valor)),
                        "data": data,
                        "descricao": descricao,
                        "saldo_apos": format(saldo_apos, '.2f')
                    }
    return nova_movimentacao

def encontra_ultima_data(num_conta,movimentacoes):
    """
    Encontra a data da última movimentação de 'num_conta' em 'movimentacoes'.
    Devolve: data encontrada (string)
    """
    i = len(movimentacoes)-1
    while i >=0:
        if movimentacoes[i]["numero_conta"] == num_conta:
            data_ultima_mov = movimentacoes[i]["data"]
            return data_ultima_mov
        i-=1

def realiza_saque(tipo,num_conta, valor, data, descricao, movimentacoes, contas):
    """
    Verifica se a operação de saque pode ser efetuada, isto é, se a conta identificada por 'num_conta' existe em 'contas' e se o 'valor' é menor ou igual
    ao saldo da conta 'num_conta'.
    Se cumprir as condições acima, encaminha os dados para a função 'movimenta()' para que a movimentação seja adicionada à 'movimentacoes'
    Devolve: lista 'contas', lista 'movimentacoes' e uma mensagem:
        - {resultado_saque}' de 'movimenta()', se cumprir os requisitos acima
        - "Saldo insuficiente", se 'valor' for maior que o saldo de 'num_conta'
        - "Esta conta não existe" se a conta 'num_conta' não existir em 'contas'
    """
    conta_aberta = verifica_conta_aberta(num_conta,contas)
    if conta_aberta:
        saldo = consulta_saldo(num_conta,contas)
        saldo_suficiente = (valor <= saldo)
        if saldo_suficiente:
            valor = -valor
            contas, resultado_saque, movimentacoes = movimenta("Saque",num_conta, valor, data, descricao, movimentacoes, contas)
            mensagem = resultado_saque
        else:
            mensagem = "Saldo insuficiente"
    else:
        mensagem = "Esta conta não existe"
        
    return contas, mensagem, movimentacoes