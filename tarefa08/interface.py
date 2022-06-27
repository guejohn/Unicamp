from contas import inicializa_contas, inicializa_movimentacoes, adiciona_conta, movimenta, consulta_saldo, gera_extrato, fecha_conta, realiza_saque

from controlador import mostra_saldo, mostra_extrato, le_varios_dados, le_dado, mostra, le_dados_movimentacao

def main():

    contas = inicializa_contas()
    movimentacoes = inicializa_movimentacoes()


    while True:
    
        operacao = input()

        if operacao == 'abrir':

            num_conta = le_dado()
            contas, resultado_abertura = adiciona_conta(num_conta,contas)
            mostra(resultado_abertura)
            

        elif operacao == 'depositar':

            num_conta,valor,data,descricao = le_dados_movimentacao()
            contas, resultado_movimentacao, movimentacoes = movimenta("Depósito",num_conta, valor, data, descricao, movimentacoes, contas)
            mostra(resultado_movimentacao)

        elif operacao == 'sacar':

            num_conta,valor,data,descricao  = le_dados_movimentacao()
            contas, resultado_saque, movimentacoes = realiza_saque("Saque",num_conta, valor, data, descricao, movimentacoes, contas)
            mostra(resultado_saque)

        elif operacao == 'saldo':

            num_conta = le_dado()
            resultado_consulta_saldo = consulta_saldo(num_conta,contas)
            mostra_saldo(resultado_consulta_saldo)


        elif operacao == 'extrato':

            num_conta, data = le_varios_dados()
            extrato, resultado_extrato = gera_extrato(num_conta, data, movimentacoes, contas)
            mostra_extrato(resultado_extrato, extrato)
            
        elif operacao == 'fechar':

            num_conta = le_dado()
            resultado_fechamento, contas = fecha_conta(num_conta, contas)
            mostra(resultado_fechamento)

        elif operacao == 'sair':
            break
        
        
main()