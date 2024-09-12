import json
import requests

class Servico:

    url = "https://tdspm-65f5c-default-rtdb.firebaseio.com/contatos.json"

    def __init__(self):
        pass

    def cadastrar_firebase(self, contato):
        contato_dict = {
            "id": contato.id,
            "nome": contato.nome,
            "telefone": contato.telefone,
            "email": contato.email,
            "nascimento": contato.nascimento.strftime("%d/%m/%Y")            
        }
        response = requests.post( self.url, json=contato_dict, timeout=100)
        return response
    
    def pesquisar_firebase(self):
        response = requests.get(self.url, timeout=100)
        contatos = json.loads(response.text)
        return list(contatos.values())