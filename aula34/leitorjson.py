import json 

arquivo = open("./dados.json", "r", encoding="utf-8")
conteudo = arquivo.read()

lista = json.loads(conteudo)

for user in lista:
    print(user["nome"])