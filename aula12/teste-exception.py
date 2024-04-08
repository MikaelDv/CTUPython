try:
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    resultado = n1 / n2
    print(f"A divisão de {n1} por {n2} é igual a {resultado}")
except ValueError:
    print("Erro! Digite um número válido.")
except ZeroDivisionError:
    print("Erro! Digite um número válido.")
except:
    print("Erro! Não foi possível executar a divisão.")
