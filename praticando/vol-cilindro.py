while True:
    try:
        raio = int(input("Qual é o raio da base do cilindro? "))
        altura = int(input("Qual é a altura do cilindro? "))
        pi = 3.14
        volume = ((raio * raio)*pi)*altura

        medida = int(input("Os dados foram fornecidos em: \n(1) - Milímetros\n(2) - Centímetros\n(3) - Metros\n(4) - Outro\n"))
        
        if(medida == 1):
            print(f"O volume do cilindro é: {volume}mm³!")
            break
        elif(medida == 2):
            print(f"O volume do cilindro é: {volume}cm³!")
            break
        elif(medida == 3):
            print(f"O volume do cilindro é: {volume}m³!")
            break
        elif(medida == 4):
            nova_medida = input("Qual a medida usada? \n")
            print(f"O volume do cilindro é: {volume} {nova_medida}³!")
            break
        else:
            print("Opção inválida. Tente novamente!")
    except:
        print("Opção inválida. Tente novamente!")
