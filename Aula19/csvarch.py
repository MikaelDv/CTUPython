arq1 = open("nomes-idades.csv", "w", encoding="utf-8")

arq1.write("Joao,(11)1111-1111,21")
arq1.write("\nMaria,(22)2222-2222,24")
arq1.write("\nJosé,(33)3333-3333,27")

arq1.close()
