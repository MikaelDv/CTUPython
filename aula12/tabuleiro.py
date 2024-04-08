preto = "    "
branco = "####"

for i in range(4):
    for i in range(3):
        for i in range(4):
            print(branco, end="")
            print(preto, end="")
        print("")
    for i in range(3):
        for i in range(4):
            print(preto, end="")
            print(branco, end="")
        print("")