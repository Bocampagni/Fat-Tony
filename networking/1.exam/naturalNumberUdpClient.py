from socket import *


serverName = gethostname()
servePort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)

print("Para fechar o cliente, digite 0.")
naturalNumber = int(input("Entre com um número: "))
if naturalNumber == 0:
    clientSocket.close()

for x in range(naturalNumber):
    clientSocket.sendto(str(x).encode(),(serverName,servePort))


clientSocket.close()
