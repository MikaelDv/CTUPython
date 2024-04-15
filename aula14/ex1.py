produtos = []

def cadastrar_produto():
    produto = {}
    produto["nome"] = input("Qual o produto deseja cadastrar?\n")
    produto["cor"] = input("Qual é a cor desse produto?\n")
    produto["valor"] = float(input(f"Qual o valor de {produto['nome']}?\n"))
    produto["unidade_medida"] = input("Em qual unidade de medida este valor está?\n")
    produtos.append(produto)

def exibir_produtos():
    for p in produtos:
        print(f"Nome: {p['nome']}")
        print(f"Cor: {p['cor']}")
        print(f"Valor do {p['unidade_medida']}: {p['valor']}")

def pesquisar_produto():
    pesquisa = input("Digite o nome do produto: ")
    for p in produtos:
        if pesquisa == p["nome"]:
            print(f"Nome: {p['nome']}")
            print(f"Cor: {p['cor']}")
            print(f"Valor do {p['unidade_medida']}: {p['valor']}")


while True:
    menu = '''
S I S T E M A  P A R A  H O R T I F R U T I
 
(A)dicionar novo produto
(L)istar todos os produtos
(P) pesquisar por um produto
(S)air do sistema
\n
Digite sua opção ==> '''

    print(menu, end="")
    opcao = input().lower()[0]

    if opcao == "a":
        cadastrar_produto()
    elif opcao == "l":
        if produtos == []:
            print("Você não possui produtos cadastrados.")
        else:
            exibir_produtos()
    elif opcao == "p":
        pesquisar_produto()
    else:
        break