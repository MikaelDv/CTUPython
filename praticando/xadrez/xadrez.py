import os

tabuleiro = [
    ["BT","BH","BB","BK","BQ","BB","BH","BT"],
    ["BP","BP","BP","BP","BP","BP","BP","BP"],
    ["","","","","","","","",],
    ["","","","","","","","",],
    ["","","","","","","","",],
    ["","","","","","","","",],
    ["WP","WP","WP","WP","WP","WP","WP","WP"],
    ["WT","WH","WB","WQ","WK","WB","WH","WT"]
]


def exibir_tabuleiro():
    os.system("cls")
    print("  ","-"*41)
    for i, linha in enumerate(tabuleiro, 1):
        print(i, " ", end="")
        for coluna in linha:
            print(f"|{coluna:^4}", end="")
        print("|")
        print("  ","-"*41)
    print("   ", end="")
    for letra in "ABCDEFGH":
        print(f"{letra:^5}", end="")
    print("\n")


def mover_peca(coluna_origem, linha_origem, coluna_destino, linha_destino):
    tabuleiro[linha_destino][coluna_destino] = tabuleiro[linha_origem][coluna_origem]
    tabuleiro[linha_origem][coluna_origem] = ""


def ler_movimento():
    mapa = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7
    }
    casa_origem = input("Qual peça deseja movimentar? (Coluna/Linha)\n").upper()
    coluna_origem = mapa[casa_origem[0]]
    linha_origem = int(casa_origem[1]) - 1
    casa_destino = input("Para qual casa deseja movimenta-la? (Coluna/Linha)\n").upper()
    coluna_destino = mapa[casa_destino[0]]
    linha_destino = int(casa_destino[1]) - 1
    mover_peca(coluna_origem, linha_origem, coluna_destino, linha_destino)


while True:
    exibir_tabuleiro()
    ler_movimento()