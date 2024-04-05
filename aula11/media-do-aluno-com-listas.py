print("Programa para calcular a média! \naritmética de 3 notas de um aluno")

lista = []

n = float(input("Por favor digite a 1ª nota: "))
lista.append(n)

n = float(input("Por favor digite a 2ª nota: "))
lista.append(n)

n = float(input("Por favor digite a 3ª nota: "))
lista.append(n)

media = (lista[0] + lista[1] + lista[2]) / 3.0
print(f"A média final é: {media:.1f}")