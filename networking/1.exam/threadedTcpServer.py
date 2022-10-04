from socket import *
import _thread


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))

serverSocket.listen(5)
print('Servidor pronto para ser usado')

def handle_client(client_socket, addr):
    while True:
        data = client_socket.recv(1024).decode().upper()
        if data == 'close': break
        print('Response to:', addr)
        print('Response data:', data)
        client_socket.send(data.encode())
    client_socket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Requisição de:", addr)
    _thread.start_new_thread(handle_client ,(connectionSocket, addr))    
