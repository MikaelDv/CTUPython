lista = [
    {'nome': 'Joao', 'telefone': '(11)1111-1111', 'idade': 21},
    {'nome': 'Maria', 'telefone': '(22)2222-2222', 'idade': 24},
    {'nome': 'José', 'telefone': '(33)3333-3333', 'idade': 27}
]

arq1 = open("./nomes-idades.csv", "w", encoding="utf-8")

for d in lista:
    arq1.write(f"{d["nome"]};{d["telefone"]};{d["idade"]}\n")

arq1.close()