arq1 = open("./nomes-idades.csv", "r", encoding="utf-8")

lista = []
linha = "-"
while linha != "":
    linha = arq1.readline().replace("\n", "")
    if linha != "":
        dados = linha.split(";")
        d = {}
        d["nome"] = dados[0].strip()
        d["telefone"] = dados[1].strip()
        d["idade"] = int(dados[2])
        lista.append(d)

print(lista)
