arq1 = open("./nomes-idades.csv", "r", encoding="utf-8")

lista = []
linha = "-"
while linha != "":
    linha = arq1.readline().replace("\n", "")
    if linha != "":
        lista.append(linha)

print("Lista: ", lista)
# linha1 = arq1.readline().replace("\n","")
# print("Linha1: ", linha1)
# linha2 = arq1.readline().replace("\n","")
# print("Linha2: ", linha2)
# linha3 = arq1.readline().replace("\n","")
# print("Linha3: ", linha3)

arq1.close()
