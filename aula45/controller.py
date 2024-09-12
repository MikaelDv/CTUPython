from servico import Servico


class Controller:

    def __init__(self):
        self.servico = Servico()

    def cadastrar(self, contato):
        print("Cadastrando o contato")
        response = self.servico.cadastrar_firebase(contato)
        print("Response: ", response)
        

    def pesquisar(self):
        print("Pesquisando contatos")
        return self.servico.pesquisar_firebase()

    def remover(self):
        print("")

    def atualiza(self):
        print("")