lista = ["Isabela", "Guilherme", "Julliana", "Mikael", "Enzo", "Vicenzo", "Guilherme"]

try:
    pos = lista.index("Guilherme", 2)
    print(f"O Guilherme esta na posição: {pos}")
except:
    print("Elemento não encontrado")

pos = lista.index("Mikael", 2)
print(f"O Mikael esta na posição: {pos}")

try:
    pos = lista.index("Jõao")
    print(f"O João esta na posição: {pos}")
except ValueError as err:
    print(f"{err}, elemento não encontrado!!")

print(lista[-1])