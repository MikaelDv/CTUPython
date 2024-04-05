linha = int(input("Quantas linhas? "))
espaco = linha - 1
print("")
for l in range(1, linha*2, 2):
    print(" "*espaco, end="")
    print("*" * l)
    espaco-=1
print(f'{" "*(linha-2)}| |')
print(f'{" "*(linha-2)}| |')