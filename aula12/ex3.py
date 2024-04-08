lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

lista_sem3 = []

i = 0

while i < 12:
    var = (lista[i] % 3)
    i += 1
    if var != 0:
        lista_sem3.append(i)

lista = lista_sem3
print(lista)