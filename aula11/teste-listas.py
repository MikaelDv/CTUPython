# lista1 = []
# lista1  = list()
# indices 0  1  2
lista1 = [7, 6, 9]

lista1.append(8)
#  0  1  2  3
# [7, 6, 9, 8]

print( "Original: ", lista1 )

lista1[2] = 8.5

print( "Depois de alterar a nota: ", lista1 )

lista1.pop(1)

print( "Depois da remoção: ", lista1 )