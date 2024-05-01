import os
from time import sleep

menu = '''** C R U D **
(C) Cadastrar
(L) Listar
(P) Procurar
(S) Sair'''

submenu = '''
(A) Alterar
(R) Remover
(M) Retornar ao Menú principal'''
carros = []


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def cadastrar(lista_carros, uso):
    veiculo = {}
    veiculo["marca"] = input(f"Qual a marca do veículo que deseja {uso}?\n").upper()
    veiculo["modelo"] = input("Qual o modelo?\n").upper()
    veiculo["ano"] = input("Qual é o ano do veículo?\n").upper()
    veiculo["placa"] = input("Por último, qual a placa do veículo?\n").upper()
    print(f"MODELO: {veiculo['modelo']} \nMARCA: {veiculo['marca']} \nANO: {veiculo['ano']} \nPLACA: {veiculo['placa']} \ncadastrado.")
    sleep(2)
    lista_carros.append(veiculo)


def listar(lista_carros):
    if lista_carros:
        for i in lista_carros:
            print(f"MARCA:{i['marca']}")
            print(f"MODELO:{i['modelo']}")
            print(f"ANO:{i['ano']}")
            print(f"PLACA:{i['placa']}")
            if i != lista_carros[-1]:
                print("~~~~~~~~~~~~~~~~~~")
        input('Pressione "enter" para voltar ao menu principal \n>')
    else:
        print("Você não possui Veículos cadastrados.")
        sleep(2)


def procurar(lista_carros):
    if not lista_carros:
        print("Você não possui veículos salvos.")
        sleep(2)
    else:
        placa = input("Qual placa deseja procurar?\n").upper()
        for i in lista_carros:
            if placa == i["placa"]:
                print(f"MARCA:{i['marca']}")
                print(f"MODELO:{i['modelo']}")
                print(f"ANO:{i['ano']}")
                print(f"PLACA:{i['placa']}")
                print(submenu)
                opc = input("> ").lower()
                if opc == "a":
                    lista_carros.remove(i)
                    cadastrar(lista_carros, "alterar")
                elif opc == "r":
                    lista_carros.remove(i)
                break
            elif i == lista_carros[-1] and i["placa"] != placa:
                print("Placa não encontrada.")
                sleep(2)


while True:
    clear()
    print(menu)
    opt = input().lower()
    if opt == "c":
        cadastrar(carros, "cadastrar")
    elif opt == "l":
        listar(carros)
    elif opt == "p":
        procurar(carros)
    else:
        break
