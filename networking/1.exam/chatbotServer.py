from socket import *
import json

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))

serverSocket.listen(1)
print('Servidor pronto para ser usado')


while True:
    connectionSocket, addr = serverSocket.accept()
    print("Conexão com:", addr)
    connectionSocket.send("Olá ! Bem vindo ! Qual o seu nome ?".encode())
    while 1:
        message = connectionSocket.recv(1024).decode()
        params = message.split("-")
        if params[0] == 0:
            connectionSocket.send("Olá ! Bem vindo ! Qual o seu nome ?\n".encode())
        
        elif params[0] == '1':
            connectionSocket.send((f"Certo, {params[1]}!\nComo posso te ajudar ?\nDigite o número que corresponde à opção desejada: \n1 - Agendar um horário de monitoria \n2 - Listar as próximas atividades da disciplina \n3 - E-mail do professor\n").encode())

        elif params[0] == '2' and params[1] not in ['1','2','3']:
            connectionSocket.send("Obrigado por utilizar nossos serviços!\nAté logo!".encode())
            break

        elif params[0] == '2':
            if params[1] == '1':
                connectionSocket.send("Para agendar uma monitoria, basta enviar um e-mail para cainafigueiredo@poli.ufrj.br\n".encode())
                connectionSocket.send("Obrigado por utilizar nossos serviços!\nAté logo!\n".encode())

            elif params[1] == '2':
                connectionSocket.send("Fique atento para as datas das próximas atividades.\nConfira o que vem por ai !\n\nP1: 28 de maio de 2022\nLista 3: 29 de maio de 2022\n".encode())
                connectionSocket.send("Obrigado por utilizar nossos serviços!\nAté logo!\n".encode())

            elif params[1] == '3':
                connectionSocket.send("Quer falar com o professor ?\nO e-email dele é sadoc@dcc.ufrj.br\n".encode())
                connectionSocket.send("Obrigado por utilizar nossos serviços!\nAté logo!\n".encode())
            
            break

        

    connectionSocket.close()