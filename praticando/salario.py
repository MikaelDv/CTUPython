while True:
    try:
        horas = int(input("Por favor, quantas horas você trabalhou no mês?\n"))
        valor_hora = int(input("Qual o valor da hora trabalhada?\nR$ "))
        per_desconto = int(input("Qual o percentual de desconto que você terá?\n% "))

        if(horas != 0 and valor_hora != 0):
            sal_brut = horas * valor_hora
            desconto = (per_desconto * sal_brut) / 100
            salario = sal_brut - desconto
            print(f"O salário final será: R$ {salario}!")
            break
        else:
            print("A quantidade de Horas e o Valor da Hora não podem ficar em branco!")

    except ValueError:
        print("Valores inválidos! Tente novamente.")
