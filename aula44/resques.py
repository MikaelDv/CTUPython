import requests
import json

url = 'https://tdspm-65f5c-default-rtdb.firebaseio.com/contatos.json'

contato = {
    "nome": "Roberto Santos",
    "telefone": "(32) 4444-4444",
    "email": "robertosantos32@teste.com"
} 

# response = requests.post(url, json=contato)

response = requests.get(url)

resposta = response.text

dict = json.loads(resposta)

print(dict["-O6Lk5oxNk6Qh4xJffYi"])

for contato in dict.values():
    print(f"Nome: {contato['nome']} - Email: {contato['email']}")