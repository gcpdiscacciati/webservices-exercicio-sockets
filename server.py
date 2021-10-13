# server.py
# coding: utf-8

import socket
import re

# Configuração da conexão
serverPort = 16000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(0)

print("Servidor pronto para receber")

# Checa se a mensagem contém números
def checkNumbers(mensagem):
    return bool(re.search("\d", mensagem))

# Checa o tamanho médio de caracteres das palavras
def avgWordLength(lista):
    soma = 0.0
    for word in lista:
        soma += len(word)
    return soma/(len(lista))

# Loop que aguarda a conexão do cliente e processa a mensagem recebida
while True:
    connectionSocket, addr = serverSocket.accept()
    print("Conexão vinda de {}".format(addr))
    message = connectionSocket.recv(2048)
    print("{} ==> {}".format(addr, message.decode('utf-8')))
    decodedMessage = message.decode('utf-8')

    # Processa a mensagem recebida
    numCaracteres = len(decodedMessage)
    possuiNumeros = checkNumbers(decodedMessage)
    listaPalavras = decodedMessage.split()
    numPalavras = len(listaPalavras)
    tamanhoMedio = avgWordLength(listaPalavras)
    modifiedMessage = (f"Número de caracteres = {numCaracteres}"
                       f"\nPossui números = {'Sim' if possuiNumeros else 'Não'}"
                       f"\nQuantidade de palavras = {numPalavras}"
                       f"\nTamanho médio de caracteres das palavras = {tamanhoMedio:.2f}")

    # Retorna a mensagem modificada
    connectionSocket.send(modifiedMessage.encode('utf-8'))

    # Encerra a conexão com o cliente
    connectionSocket.close()
