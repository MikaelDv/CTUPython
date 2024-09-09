import socket

HOST = "127.0.0.1"
PORT = 10000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Servidor criado")

servidor.bind( (HOST, PORT) )
print(f"Servidor conectado na interface {HOST} na porta {PORT}")

servidor.listen()
print(f"Aguardando cliente se conectar na porta {PORT}")

cliente_conexao, cliente_addr = servidor.accept()
print(f"Cliente no endereço: {cliente_addr} conectou no servidor")

with open('./index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

response = f"""
HTTP/1.1 200 OK
Date: Thu, 05 Sep 2024 11:54:00 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Thu, 05 Sep 2024 10:15:56 GMT
Content-Length: {len(html_content)}
Content-Type: text/html
Connection: Closed

{html_content}"""

cliente_conexao.sendall(response.encode("utf-8"))

while True:
    mensagem_bytes = cliente_conexao.recv(1024)
    texto = mensagem_bytes.decode("utf-8")
    #print("Mensagem Recebida do cliente: ", mensagem_bytes.decode("utf-8"))
    print(texto, end="")
    if texto=="X":
        break

cliente_conexao.close()