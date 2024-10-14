import json
import requests

class Funcionario:
    matricula = ""
    nome = ""
    salario = 0.0

    def __init__(self, matricula="", nome="", salario=0.0):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario
        
        
    def to_dict(self):
        return {
            "matricula": self.matricula,
            "nome": self.nome,
            "salario": self.salario
        }
    
    
    def from_dict(self, dic):
        novo_func = Funcionario()
        novo_func.matricula = dic["matricula"]
        novo_func.nome = dic["nome"]
        novo_func.salario = dic["salario"]
        return novo_func


    def __str__(self):
        return f""" +-+ Funcionario +-+
Matrícula: {self.matricula}
Nome: {self.nome}
Salário: {self.salario}
+{"-" * (len(self.nome) + 6)}+
    """
        
enzo = Funcionario()
print(enzo)

class Apresentacao:    
    def menu_principal(self):
        print("(C) - Cadastrar")
        print("(L) - Ler Todos")
        print("(S) - Sair")
        print("Digite a sua opção: ", end="")
        opt = input()
        opt_tratada = str(opt)[0].upper()
        match(opt_tratada):
            case "C":
                self.cadastrar()
            case "L":
                self.ler_todos()
            case "S":
                self.exit()
            case _: 
                print("Opção inválida!")
    
    def cadastrar(self):
        novo_func = Funcionario()
        print("+-+ CADASTRO +-+")
        mat = input("Matrícula: ")
        while mat == "":
            mat = input("\nO campo 'Matrícula' não pode ficar vazio. \nPor favor, preencha corretamente.\n\nMatrícula: ")
        novo_func.matricula = mat
        nome = input("Nome: ")
        while nome == "":
            nome = input("\nO campo 'Nome' não pode ficar vazio. \nPor favor, preencha corretamente.\n\nNome: ")
        novo_func.nome = nome
        sal = input("Salário: ")
        while sal == "":
            sal = input("\nO campo 'Salário' não pode ficar vazio. \nPor favor, preencha corretamente.\n\nSalário: ")
        try:
            novo_func.salario = float(sal)
        except:
            print("Valor Inválido !!")
        return novo_func


class Repositorio():
    URL_BASE = ""
    lidos_firebase = []
    
    def __init__(self):
        self.URL_BASE = "https://tdspm-65f5c-default-rtdb.firebaseio.com"
        self.lidos_firebase = []
        
    
    def gravar(self, param) -> bool:
        resposta = requests.post(url= self.URL_BASE + "/funcionarios.json", json=param, timeout=5)
        if resposta.status_code == 200:
            return True
        else:
            print(resposta.text)
            return False
        
    def ler_todos(self):
        resposta = requests.get(url = self.URL_BASE + "/funcionarios.json", timeout=5)
        corpo_resposta = resposta.json()
        for funcionario in corpo_resposta.values():
            novo_func = Funcionario()
            novo_func.matricula = funcionario["matricula"]
            novo_func.nome = funcionario["nome"]
            novo_func.salario = funcionario["salario"]
            self.lidos_firebase.append(novo_func)    
            
repo = Repositorio()
repo.ler_todos()
for func in repo.lidos_firebase:
    print(func)
