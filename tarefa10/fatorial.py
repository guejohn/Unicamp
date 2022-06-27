
def fatorial(numero):
    """
    Calcula o fatorial de 'número'
    """
    if numero == 0:
        return 1
    
    else:
        resultado = numero * fatorial(numero-1)
        return resultado


def main():
    numero = int(input())
    resultado = fatorial(numero)
    print(resultado)

main()