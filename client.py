# client.py
# coding: utf-8

import socket

#IP do servidor, deve ser alterado caso cliente e servidor não estejam na mesma máquina
serverName = '127.0.0.1'
serverPort = 16000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Recebe a mensagem do cliente
message = input("Escreva uma frase: ")

# Envia a mensagem para o servidor
clientSocket.send(message.encode('utf-8'))

# Recebe e imprime a mensagem processada
modifiedMessage = clientSocket.recv(1024)
print(modifiedMessage.decode('utf-8'))

clientSocket.close()