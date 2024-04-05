"""
Utilizando as ténicas para popular listas e somar
valores da lista, crie um programa para calcular
a media de crescimento semanal de uma planta. Para isto
o programa deverá pedir a altura da planta medida na
semana, por 10 semanas. Com base na soma destas alturas
calcule a média de crescimento ao longo das semanas.
"""

print("Programa para calcular a média de crescimento \nsemanal de uma planta.")

lista_tam = []

n1 = float(input("Digite a altura da planta na primeira semana em cm's: "))
lista_tam.append(n1)

for i in range(9):
    n = float(input(f"Digite a altura da planta medida na {i + 2}ª semana em cm's: "))
    lista_tam.append(n)


crescimento = lista_tam[9] - lista_tam[0]
media_crescimento = (lista_tam[9] - lista_tam[0]) / 9

print(f"Crescimento total foi: {crescimento}cm \nMédia de crescimento: {media_crescimento:.2f}cm/semana")
