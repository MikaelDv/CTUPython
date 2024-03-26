a = 79

# Como pegar este valor da variavel (a)
# como sendo octal

a_em_octal = oct(a)
print("A em octal: ", a_em_octal)

# Bases numéricas
# Algarismos Binários: 0 ou 1
# Algarismos Octais: 0, 1, 2, 3, 4, 5, 6, 7
# ALgarismos Decimais: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# Algarismos Hexadecimais: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

n1 = 8120990732 # 8.170.990.732
numero_em_binario = bin(n1)
numero_em_octal = oct(n1)
print("N1: ", n1)
print("N1 binário: ", bin(n1))
print("N1 em Octal: ", oct(n1))
print("N1 em Hexadecimal: ", hex(n1))

s = "Ola Mundo !!!"
print(" Texto: " + s)

s_minusculo = s.lower()  # "ola mundo !!!"
print("Texto Minusculo: " + s_minusculo)

s_maiusculo = s.upper()
print("Texto Maiusculo: " + s_maiusculo)

tamanho = len( s )  # int    13
print("Tamanho da string: ", tamanho)
print("Tamanho da string: " + str(tamanho))
#        01234567890123456789012345678901
texto = "A FIAP é uma faculdade bem legal"
tam = len(texto)
print("Tamanho: ", tam)
letra = texto[17]
print("Letra na posicao 17: " + letra)
letra = texto[20]
print("Letra na posicao 20: " + letra)

pos = texto.find( "legal" )
print("O texto possui a palavra", 
      "legal na posicao: ", pos)

pos = texto.find( "FIAP" )
print("O texto possui a palavra", 
      "FIAP na posicao: ", pos)

pos = texto.find( "manhã" )
print("O texto possui a palavra", 
      "manhã na posicao: ", pos)

pos = texto.find( "m" )
print("O texto possui a letra m ",
      "na posição: ", pos)

pos = texto.find( "m", 11 )
print("O texto possui outra letra m ",
      "na posição: ", pos)

pos = texto.find( "m", 26 )
print("O texto possui outra letra m ",
      "na posição: ", pos)
print(hex(898908))