num_lances = 0
maior_lance = 0
lista_output = []
lance_anterior = 0

comando = str(input())
codigo_produto, lance_minimo = input().split()
lista_output.append(f"Bem-vindo ao Leilão de Algoritmópolis! Produto {codigo_produto} com lance mínimo R$ {lance_minimo}")
comando = str(input())

while comando != 'F':

    if comando=='L':
        nome, lance = input().split()

        if float(lance) >= float(lance_minimo) and float(lance) > float(lance_anterior):
            lista_output.append(f"{nome} deu um lance de R$ {lance}")
            num_lances +=1
            lance_anterior = lance

            if float(lance) > float(maior_lance):
                maior_lance = lance
                nome_maior_lance = nome

        else:
            lista_output.append(f"Lance inválido de {nome}")

    elif comando=='S':
        lista_output.append(f"Status do Leilão do Produto {codigo_produto}")
        if num_lances>0:
            lista_output.append(f"{num_lances} lances até agora")
            lista_output.append(f"{nome_maior_lance} deu o melhor lance, de valor R$ {maior_lance}")
        else:
            lista_output.append("Não houve lances")
    
    comando = input()

if comando == 'F':
    lista_output.append(f"Leilão finalizado com {num_lances} lances") 
    lista_output.append(f"{nome_maior_lance} venceu com o lance de valor R$ {maior_lance}") 

for i in lista_output:
    print(i)

    