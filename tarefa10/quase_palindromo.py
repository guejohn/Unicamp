def palavra_ao_contrario(palavra):
    """
    Dada 'palavra', gera um string com os caracteres ao contrário
    Retorna: string gerada 'contrario'
    """
    contrario = ""
    for i in range(len(palavra)-1, -1, -1):
            contrario += str(palavra[i])

    return contrario

def quase_palindromo(k, palavra, contrario = "", i = 0, contador_diferencas = 0):
    """
    Imprime "sim" se 'palavra' for um quase palíndromo, isto é, se, ao compará-la com o seu inverso, tiver no máximo 'k' caracteres diferentes.
    Do contrário, imprime "nao".
    """
    if contrario == "":
        contrario = palavra_ao_contrario(palavra)

    if i == len(palavra) - 1:

        if contador_diferencas <= k:
            print("sim")

        else:
            print("nao")
            
        return None

    if palavra[i] != contrario[i]:
        contador_diferencas += 1

    i += 1

    return quase_palindromo(k, palavra, contrario, i, contador_diferencas)

def main():
    k = int(input())
    palavra = input()
    quase_palindromo(k, palavra)


main()
