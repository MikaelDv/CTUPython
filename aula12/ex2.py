qtd = int(input("Quantos nomes deseja armazenar?\n:"))

lista_nomes = []

for i in range(qtd):
    nome = input(f"{i+1}° nome: ")
    lista_nomes.append(nome)

for i in range(qtd):
    print(lista_nomes[-(i+1)])

print(lista_nomes)