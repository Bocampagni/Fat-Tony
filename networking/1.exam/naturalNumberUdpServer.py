from socket import * 

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)

serverSocket.bind(('',serverPort))

print('O servidor está pronto para uso')

while True:
    number, clientAdress = serverSocket.recvfrom(2048)
    print(number.decode())
