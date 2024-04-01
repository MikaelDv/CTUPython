coluna = int(input("Quantas colunas deseja? "))
linha = int(input("Quantas linhas deseja? "))
for i in range(0, linha):
    for j in range(1, coluna+1):
        print(j, end="")
    print("")

