# client.py
# coding: utf-8

import socket

serverName = '127.0.0.1'
serverPort = 16000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = input("Escreva uma frase: ")

clientSocket.send(message.encode('utf-8'))

modifiedMessage = clientSocket.recv(1024)
print(modifiedMessage.decode('utf-8'))

clientSocket.close()