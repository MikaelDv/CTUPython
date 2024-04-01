linha = int(input("Quantas linhas?"))
espaco = linha - 1
print()
for l in range(1, linha*2, 2):
    if l == 1:
        print(" "*espaco, end="")
        print("*")
        espaco-=1
    elif l == (linha*2) - 1:
        print("*" * l)
    else:
        print(" "*espaco, end="")
        print("*" + " "*l + "*")
        espaco-=1
print(f'{" "*(linha-2)}| |')
print(f'{" "*(linha-2)}| |')
