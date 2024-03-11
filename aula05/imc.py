peso = float(input("Qual é o seu peso?\n"))
altura = int(input("Qual é a sua altura em centímetros?"))

imc = peso/((altura/100)**2)
print(imc)

if imc >= 25:
    print(f"Seu IMC é: {round(imc, 1)}. Você precisa emagrecer!")
elif imc <= 18.5:
    print(f"Seu IMC é: {round(imc, 1)}. Você precisa ganhar massa!")
else:
    print(f"Seu IMC é: {round(imc, 1)}. Você está saudável!")