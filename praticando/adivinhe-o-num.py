import random as rdm
print("/*******BEM-VINDO AO JOGO DO NÚMERO SECRETO*******/")

def main():
    possibilidade = []
    dificuldade = int(input("De 1 a 1000, qual o nível de dificuldade desejado?\n"))

    while(dificuldade != 0):
        possibilidade.append(dificuldade)
        dificuldade -= 1

    num_secreto = rdm.choice(possibilidade)
    tentativa = 0
    tentativas = 0

    while(num_secreto != tentativa):
        pergunta = int(input("Qual é o número secreto? \n"))
        tentou = tentativa + pergunta
        tentativas += 1
        if(num_secreto >  tentou):
            print(f"O número secreto é maior que {tentou}!")
        elif(num_secreto < tentou):
            print(f"O número secreto é menor que {tentou}!")
        else:
            print(f"**Você acertou o número secreto, {num_secreto}!**")
            print(f"**********Com {tentativas} tentativas!**********")
            break

def jogar_novamente():
    while True:
        try:
            main()
            jogar_nvmt = input("Deseja jogar novamente? (Y/n) ")
            if(jogar_nvmt.lower() != "y"):
                break
        except:
            print("Opção inválida! Tente novamente.")

jogar_novamente()