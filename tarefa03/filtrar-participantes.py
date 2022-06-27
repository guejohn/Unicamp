lista_nomes = []

N, Q, V, M, a, b = input().split()
for _ in range(int(N)):
    nome, q, v = input().split()  
    if (int(v)>0):
        soma = 0
        for _ in range(int(v)):
            soma += float(input())
        if int(v) >= int(V):
            if (soma/int(v) >= float(M)):
                lista_nomes.append(nome)

    if (int(q)>=int(Q)) or (nome[0]==a) or (nome[0]==b):
        if nome not in lista_nomes:
            lista_nomes.append(nome)

for nome in lista_nomes:   
    print(nome)
    

    