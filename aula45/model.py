from datetime import datetime

class Contato:
    """
        Classe que descreve os objetos do tipo Contato
    """
    id = ""
    nome = ""
    telefone = ""
    email = ""
    nascimento = datetime.now

    def __init__(self, id="", nome="", telefone="", email="", nascimento=datetime.now):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.nascimento = nascimento

    def __str__(self):
        return f"""({self.id} - {self.nome} 
                    {self.telefone} 
                    {self.email}
                    {self.nascimento.strftime("%d/%m/%Y")})"""

if __name__ == "__main__":
    date_time_str = "01/04/2003"
    nascimento = datetime.strptime(date_time_str, "%d/%m/%Y")
    c1 = Contato("0001", "João Silva", "(11) 1111-1111", "joao@teste.com", nascimento)
    # c1.id = "0001"
    # c1.nome = "João Silva"
    # c1.telefone = "(11) 1111-1111"
    # c1.email = "joao@teste.com"
    # date_time_str = "01/04/2003"
    # c1.nascimento = datetime.strptime(date_time_str, "%d/%m/%Y")

    print("Contato: ", c1)