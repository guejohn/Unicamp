Q = 3
V = 2
M = 120.45
a = 'D'
b = 'R'
soma =0

nome = input("Qual o seu nome: ")
num_leiloes = int(input("Quantos leilões já participou antes: "))

if num_leiloes>=0:
    num_lances = int(input("Quantos lances você já venceu: "))

    if num_lances>=V:
        for i in range(2):
            print(f"Lance vencedor {i+1}: ",end = '')
            lance = float(input())
            soma += lance
            
        if ((soma/num_lances) >= M) or (num_leiloes>=Q) or (nome[0] == a) or (nome[0] == b):
            print("Parabéns! Você pode se inscrever.")

        else:
            print("Infelizmente, você não poderá participar nesse ano.")   

    elif (num_leiloes>=Q):
        print("Parabéns! Você pode se inscrever.")

    elif (nome[0] == a) or (nome[0] == b):
            print("Parabéns! Você pode se inscrever.")

    elif num_lances<V:
        print("Infelizmente, você não poderá participar nesse ano.")

else:
    print("Infelizmente, você não poderá participar nesse ano.") 