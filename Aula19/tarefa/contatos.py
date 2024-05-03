import os
from time import sleep

lista_contatos = []

menu = '''*** Lista de Contatos ***
(C) - Cadastrar
(L) - Listar
(P) - Procurar
(B) - Backup em um arquivo
(R) - Restaurar de um arquivo
(S) - Sair'''

submenu = '''
(A) - Alterar
(R) - Remover
(M) - Retornar ao Menú principal'''


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def cadastrar(lista):
    contato = {
        "nome": input("Digite o nome do contato: "),
        "telefone": input("Digite o telefone: "),
        "email": input("Digite o email: ").lower(),
        "peso": float(input("Digite o peso dessa pessoa: "))
    }
    lista.append(contato)


def listar(lista):
    if lista:
        for ctt in lista:
            if ctt == lista[0]:
                print(f"{'*'*14} Contatos {'*'*14}")
            print(f"Nome: {ctt['nome']: >32}")
            print(f"Telefone: {ctt['telefone']: >28}")
            print(f"Email: {ctt['email']: >31}")
            print(f"Peso: {ctt['peso']: >32}")
            print("*" * 38)
        input('Pressione "enter" para voltar ao menú.\n')
    else:
        print("Você não possui contatos salvos!")
        sleep(1.5)


def procurar(lista):
    if not lista:
        print("Você não possui contatos salvos.")
    else:
        email = input("Digite o email a ser procurado: ").lower()
        for ctt in lista:
            if email == ctt["email"]:
                print(f"\n{'*'*9} Resultado Pesquisa {'*'*9}")
                print(f"Nome: {ctt['nome']: >32}")
                print(f"Telefone: {ctt['telefone']: >28}")
                print(f"Email: {ctt['email']: >31}")
                print(f"Peso: {ctt['peso']: >32}")
                print("*" * 38)
                print(submenu)
                opc = input("> ").lower()
                if opc == "a":
                    lista.remove(ctt)
                    cadastrar(lista)
                elif opc == "r":
                    lista.remove(ctt)
                    print("Contato removido da lista!")
                    sleep(1.5)
                break
            elif ctt == lista[-1] and ctt["email"] != email:
                print("Contato não encontrado.")
                sleep(1.5)


def backup(lista):
    if lista:
        arquivo = open("./contatos.csv", "w", encoding="utf-8")
        for ctt in lista:
            arquivo.write(f"{ctt['nome']};{ctt['telefone']};{ctt['email']};{ctt['peso']}\n")
        arquivo.close()
        print("Contatos salvos com sucesso!")
        sleep(1.5)
    else:
        print("Você não possui contatos registrados!")
        sleep(1.5)


def restaurar(lista):
    try:
        arquivo = open("./contatos.csv", "r", encoding="utf-8")
        linha = "-"
        while linha != "":
            linha = arquivo.readline().replace("\n", "")
            if linha != "":
                dados = linha.split(";")
                ctt = {
                    "nome": dados[0],
                    "telefone": dados[1],
                    "email": dados[2],
                    "peso": dados[3]
                }
                if lista:
                    for c in lista:
                        if c["email"] == ctt["email"]:
                            break
                        if c == lista[-1] and c["email"] != ctt["email"]:
                            lista.append(ctt)
                else:
                    lista.append(ctt)
        print("Contatos importados com sucesso!")
        sleep(1.5)
    except FileNotFoundError:
        print("Você não possui uma lista de contatos salva.")
        sleep(1.5)


while True:
    clear()
    print(menu)
    opt = input("> ").lower()
    if opt == "c":
        clear()
        cadastrar(lista_contatos)
    elif opt == "l":
        clear()
        listar(lista_contatos)
    elif opt == "p":
        clear()
        procurar(lista_contatos)
    elif opt == "b":
        clear()
        backup(lista_contatos)
    elif opt == "r":
        clear()
        restaurar(lista_contatos)
    elif opt == "s":
        break
