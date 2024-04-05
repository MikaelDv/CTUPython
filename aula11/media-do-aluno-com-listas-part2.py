print("Programa para calcular a média! \naritmética de 3 notas de um aluno")

lista = []

for i in range(3):
    n = float(input(f"Por favor digite a {i + 1}ª nota: "))
    lista.append(n)

soma = 0
for i in range(3):
    numero = lista[i]
    soma = soma + numero
    print(f"Numero: {numero}, Soma: {soma}")

media = soma / 3
print(f"Média é: {media:.1f}")