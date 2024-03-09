import random

possibilidade = [ 1, 2, 3]
escolha_pc = random.choice(possibilidade)
dicionario = {1:"Pedra",2:"Papel",3:"Tesoura"}

print("(1)-Pedra\n(2)-Papel\n(3)-Tesoura")
tentativa = int(input())

if(escolha_pc == 3 and tentativa == 1):
    print(f"Você ganhou! \nUsuário: {dicionario[tentativa]} \nPC: {dicionario[escolha_pc]}")
elif(escolha_pc == tentativa):
    print(f"Empate! \nUsuário: {dicionario[tentativa]} \nPC: {dicionario[escolha_pc]}")
elif(escolha_pc == 1 and tentativa == 3):
    print(f"Você perdeu... \nUsuário: {dicionario[tentativa]} \nPC: {dicionario[escolha_pc]}")
elif(escolha_pc > tentativa):
    print(f"Você perdeu... \nUsuário: {dicionario[tentativa]} \nPC: {dicionario[escolha_pc]}")
else:
     print(f"Você ganhou! \nUsuário: {dicionario[tentativa]} \nPC: {dicionario[escolha_pc]}")