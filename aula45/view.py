from datetime import datetime
import os
from controller import Controller
from model import Contato

class View:
    rodando = True
    def __init__(self):
        self.control = Controller()
        pass

    def ler_dados_contato(self):
        novo_contato = Contato()
        print("Digite os dados do contato")
        novo_contato.nome = input("Nome: ")
        novo_contato.email = input("Email: ")
        novo_contato.telefone = input("Telefone: ")
        date_time_str = input("Nascimento: ")
        nascimento = datetime.strptime(date_time_str, "%d/%m/%Y")
        novo_contato.nascimento = nascimento
        return novo_contato

    def menu_principal(self):
        os.system("CLS")
        print("Agenda de Contato no Firebase")
        print("Menu Principal")
        print("(1) - Cadastrar novo contato")
        print("(2) - Procurar contatos existentes")
        print("(3) - Remover um contato especifico")
        print("(4) - Atualizar um contato especifico")
        print("(5) - Sair do sistema")
        opcao = input("Por favor escolha uma opção e tecle <ENTER>: ")
        if len(str(opcao)) > 0:
            opcao = str(opcao)[0]
            match opcao:
                case '1':
                    self.control.cadastrar(self.ler_dados_contato())
                case '2':
                    contatos = self.control.pesquisar()
                    for contato in contatos:
                        print("="*40)
                        print(contato)
                case '3':
                    self.control.remover()
                case '4':
                    self.control.atualizar()
                case '5':
                    print("Obrigado por usar o nosso sistema. Até Breve!")
                    self.rodando = False
                case _:
                    print("Opção inválida")
        else:
            print("Você precisa selecionar uma opção")

    def executar(self):
        while self.rodando:
            self.menu_principal()
            input("Tecle <ENTER> para continuar")

if __name__ == "__main__":
    view = View()
    view.executar()