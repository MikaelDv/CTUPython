import random 
from http.server import BaseHTTPRequestHandler, HTTPServer

def numeros_mega_sena():
    premiado = []
    index = 0
    while index < 6:
        num = random.randint(1,60)
        if num not in premiado: 
            premiado.append(num)
            index += 1
    return premiado

class MeuRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Cliente se conectou e pediu um GET")
        self.send_response(200)
        self.send_header("content_type", "text/plain")
        self.end_headers()
        self.wfile.write(b"servidor de Numeros da Mega sena\n")
        self.wfile.write(f"{numeros_mega_sena()}".encode('utf-8'))

print("Iniciando Servidor")
servidor = HTTPServer( ('127.0.0.1', 80), MeuRequestHandler )
print("Aguardando conexão...")
servidor.serve_forever()