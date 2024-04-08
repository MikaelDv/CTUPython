lista = ["Pedro", "João", "Maria", "Pedro"]
print("Lista original: ", lista)

tamanho = len(lista)
print("Tamanho: ", tamanho)

lista.insert(1,"Matheus")
tamanho = len(lista)
print("Lista com Matheus: ", lista)

lista.pop(3)
print("Lista sem a Maria: ", lista)

pedros = lista.count("Pedro")
print(f"Há {pedros} Pedros na lista")

lista.remove("Pedro")
pedros = lista.count("Pedro")
print(f"Há {pedros} Pedros na lista")

print("Lista sem o Pedro: ", lista)