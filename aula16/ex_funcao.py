def validar():
    while True:
        teste = input("Digite um número inteiro: ")
        try:
            teste_int = int(teste)
            print("Isso é um número inteiro! Número: ", teste_int)
            break
        except:
            print("Isso NÃO é um NÚMERO inteiro!")
        
validar()
