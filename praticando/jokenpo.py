import random

total_jogos = 0
acertos = 0
porcentagem = 0

def main():
    global total_jogos, acertos, porcentagem

    possibilidade = [ 1, 2, 3]
    escolha_pc = random.choice(possibilidade)
    dicionario = {1:"Pedra",2:"Papel",3:"Tesoura"}

    print("JO-KEN-PO!")
    print("(1)-Pedra\n(2)-Papel\n(3)-Tesoura")
    jogada = int(input())

    if(escolha_pc == 3 and jogada == 1):
        total_jogos += 1
        acertos += 1
        porcentagem = (acertos / total_jogos) * 100
        print(f"Você ganhou! \nUsuário: {dicionario[jogada]} \nPC: {dicionario[escolha_pc]} \nPorcentagem de nggr: {round(porcentagem, 1)}%")     
    elif(escolha_pc == jogada):
        total_jogos += 1
        porcentagem = (acertos / total_jogos) * 100
        print(f"Empate! \nUsuário: {dicionario[jogada]} \nPC: {dicionario[escolha_pc]} \nPorcentagem de nggr: {round(porcentagem, 1)}%")
    elif(escolha_pc == 1 and jogada == 3):
        total_jogos += 1
        porcentagem = (acertos / total_jogos) * 100
        print(f"Você perdeu... \nUsuário: {dicionario[jogada]} \nPC: {dicionario[escolha_pc]} \nPorcentagem de nggr: {round(porcentagem, 1)}%")
    elif(escolha_pc > jogada):
        total_jogos += 1
        porcentagem = (acertos / total_jogos) * 100
        print(f"Você perdeu... \nUsuário: {dicionario[jogada]} \nPC: {dicionario[escolha_pc]} \nPorcentagem de nggr: {round(porcentagem, 1)}%")
    else:
        total_jogos += 1
        acertos += 1
        porcentagem = (acertos / total_jogos) * 100
        print(f"Você ganhou! \nUsuário: {dicionario[jogada]} \nPC: {dicionario[escolha_pc]} \nPorcentagem de nggr: {round(porcentagem, 1)}%")

def jogar_novamente():
    global porcentagem
    while True:
        try:
            jogar_nvmt = input("Deseja jogar novamente? (Y/n) ")
            if(jogar_nvmt.lower() != "y"):
                print(f"Finalizando o jogo com {round(porcentagem, 1)}% de acertos!")
                break
            else:
                main()
        except:
            print("Opção inválida! Tente novamente.")

main()

jogar_novamente()