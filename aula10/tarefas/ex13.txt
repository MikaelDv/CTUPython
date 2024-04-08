col = int(input("Quantas colunas deseja printar? "))

lin = int(input("Quantas linhas? "))

for i in range(lin):
    num = 1
    for i in range(col):
        print(num, end="")
        num+=1
    print("")