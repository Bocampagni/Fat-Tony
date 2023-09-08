from socket import *


serverName = gethostname()
servePort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)

print("Para fechar o cliente, digite 0.")
while True:
    message = input("Entre com a mensagem em minusculo: ")
    if message == '0':
        break
    clientSocket.sendto(message.encode(),(serverName,servePort))

    modifiedMessage, serverAdress = clientSocket.recvfrom(2048)
    print("Resposta do servidor: ", modifiedMessage.decode())


clientSocket.close()