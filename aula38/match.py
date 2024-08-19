menu = """
        (1) - Cadastrar
        (2) - Mostrar
        (3) - Remover
        (4) - Atualizar
        (5) - Sair
        
        >"""

while True:
    print(menu, end="")
    escolha = int(input()[0])
    match escolha:
        case 1:
            print("Cadastrou colega!")
        case 2:
            print("Mostrei ja")
        case 3: 
            print("Removendo mano")
        case 4: 
            print("Atualizacao de software em andamento")
        case 5:
            print("Tchau!")
            break
        case _:
            print(escolha, type(escolha))
            print("Opção inválida!")

        