while True:
    print("Qual é o seu nome?")
    nome = input()
    print(f"{nome} qual foi a sua no primeiro trimestre?")
    n1 = float(input())
    print("E no segundo trimestre?")
    n2 = float(input())
    print("E no terceiro?")
    n3 = float(input())
    media = (n1 + n2 + n3) / 3 

    print("Nome:      Nota1:      Nota2:      Nota3:      Média Final:")
    print(f"{nome:<11}{n1:<12}{n2:<12}{n3:<12}{media:>12.1f}")

    nvmt = input("Você deseja executar novamente? (S/N)").lower()
    if nvmt != "n":
        break

