# server.py
# coding: utf-8

import socket
import re

serverPort = 16000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(0)

print("Servidor pronto para receber")

def checkNumbers(mensagem):
    return bool(re.search("\d", mensagem))

def avgWordLength(lista):
    soma = 0.0
    for word in lista:
        soma += len(word)
    return soma/(len(lista))

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Conexão vinda de {}".format(addr))
    message = connectionSocket.recv(2048)
    print("{} ==> {}".format(addr, message.decode('utf-8')))
    decodedMessage = message.decode('utf-8')
    numCaracteres = len(decodedMessage)
    possuiNumeros = checkNumbers(decodedMessage)
    listaPalavras = decodedMessage.split()
    numPalavras = len(listaPalavras)
    tamanhoMedio = avgWordLength(listaPalavras)
    modifiedMessage = (f"Número de caracteres = {numCaracteres}"
                       f"\nPossui números = {'Sim' if possuiNumeros else 'Não'}"
                       f"\nQuantidade de palavras = {numPalavras}"
                       f"\nTamanho médio de caracteres = {tamanhoMedio: .2f}")

    
    connectionSocket.send(modifiedMessage.encode('utf-8'))
    connectionSocket.close()
