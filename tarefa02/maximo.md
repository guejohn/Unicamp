2)

a) As variáveis e seus respectivos tipos são:
    lista : list
    maximo: int
    valor: int
    numero_digitado: int


b) As estruturas de controle presentes nos dois algoritmos são o for, o if e o while, que correspondem, respectivamente, à interação limitada, execução condicional e iteração condicional.

O formato geral da estrutura 'for' é dado por 'for', uma variável, 'in', uma lista ou função 'range()' e ':'. A váriavel posterior ao 'for' assumirá cada valor percorrido pela lista ou pela função range().

for (variável) in (lista/range()) :
    ...

Já o formato geral da estrutura if é dado por 'if', uma expressão e ":". A expressão é dada pela comparação de dois ou mais elementos e retornará um valor booleano, como 'True' ou 'False', sendo que o bloco de comandos que vem abaixo do 'if' só será executado se a expressão retornar o valor 'True'

if (expressão):
    ...

Por fim, o formato geral da estrutura while é dado por 'while', uma expressão e ':'. A expressão é dada pela comparação de dois ou mais elementos e, enquanto a condição for verdadeira, o bloco de instruções abaixo do 'while' será executado repetidamente, até que a condição se torne falsa.

while (expressão):
    ...


c) Utilizamos a iteração condicional no exemplo 2. 

Seria possível reescrever o algoritmo 1 trocando o "for" por "while" se utilizássemos uma variável auxiliar contadora:


lista = [1, -3, 4, 2, -5]
maximo = lista[0]
i = 0
while i<5:
    if lista[i] > maximo:
        maximo = lista[i]
    i+=1
print(maximo)

No entanto, não seria possível reescrever o 2° algoritmo substituindo o while por for já que, como o número de entradas é indefinido, não conseguimos utilizar uma iteração limitada.




    
