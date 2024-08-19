lista = ["Enzo", "Mikael", "Julliana", "Karol"]

match lista:
    case [*nomes]:
        for i, nome in enumerate(nomes):
            print(i, "-", nome)