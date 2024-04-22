arquivo = open("./nomes.txt", "r", encoding="UTF-8")
texto = arquivo.readlines()
arquivo.close

arquivo_novo = open("./teste.txt", "w", encoding="UTF-8")
for linha in texto:
    arquivo_novo.write(linha)
arquivo_novo.close
