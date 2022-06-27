1.a) A entrada do problema é composta por duas informações: uma data, a qual deve conter o dia, mês e ano; e o número de dias que o usuário gostaria de adicionar à data fornecida. Já o conjunto de saída é composto por uma nova data, com o mesmo formato de dia, mês e ano. A relação entre as datas e o número de dias a ser adicionado é que deve-se adicionar o número de dias à data obedecendo a a data final do mês em questão, já que nem todo mês do ano possui a mesma quantidade de dias. 

b) Lista de instruções elementares permitidas:
    - somar números

Algoritmo:

1 - Leia a data e o número de dias a serem adicionados a essa data
2 - Verifique quantos dias possui o mês especificado pela data.
3 - Some o número de dias a serem adicionados a data, mantendo o mês da data original, até que o dia da data atinja o número de dias do mês.
4 - Se o dia é maior do que o número de dias do mês e o mês é diferente de 12, acrescente +1 ao mês e some o restante dos dias à data, repetindo o passo 3 até que o número seja completamente somado à data. 
5 - Se o dia é maior do que o número de dias do mês e o mês é igual a dezembro (12), substitua o mês por 1, acrescente +1 ao ano e volte para o passo 3, repetindo o passo 3 até que o número seja completamente somado à data. 
6 - Mostre a nova data.
