def numeros():
    n1 = int(input("digite o primeiro n°: "))
    n2 = int(input("digite o segundo n°: "))
    return n1, n2


def soma():
    n1, n2 = numeros()
    print("resultado: ", n1 + n2)


def sub():
    n1, n2 = numeros()
    print("resultado: ", n1 - n2)


def mult():
    n1, n2 = numeros()
    print("resultado: ", n1 * n2)


def div():
    n1, n2 = numeros()
    print("resultado: ", n1 / n2)


functions = {
    1: soma,
    2: sub,
    3: mult,
    4: div
}

option = int(input('''(1) - Somar
(2) - Subtrair
(3) - Multiplicar
(4) - Dividir\n>'''))


functions[option]()
