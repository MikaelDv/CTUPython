lin = int(input("Quantas linhas terá o seu triangulo? "))

for i in range(lin):
    lin-=1
    print(" " * lin, end="")
    print("*" * (i+1))
