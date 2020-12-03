from random import randint
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
     connectionSocket, addr = serverSocket.accept()
     sentence = connectionSocket.recv(1024).decode()
     print(f'server received: {sentence}')
     capitalizedSentence = sentence.upper()
     if randint(1, 10) > 4:
          connectionSocket.send(capitalizedSentence.encode())
     else:
          print('lost')
     connectionSocket.close()
