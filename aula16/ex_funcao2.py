def validar(String):
    while True:
        teste = input(String)
        try:
            teste_int = int(teste)
            print("Isso é um número inteiro! Número: ", teste_int)
            break
        except:
            print("Isso NÃO é um NÚMERO inteiro!")
    return teste_int
        
ano = validar("Informe o ano de nascimento: ")
dia = validar("Informe o dia do nascimento: ")

print(ano + dia)