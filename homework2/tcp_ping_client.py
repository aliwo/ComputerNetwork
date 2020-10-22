from socket import *
from time import process_time


SERVER_NAME = 'localhost'
SERVER_PORT = 12000
MESSAGE = 'ping'

def ping(shot):
    loss = 0
    for i in range(1, shot + 1):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((SERVER_NAME, SERVER_PORT))
        start = process_time()
        try:
            clientSocket.send(MESSAGE.encode())
            modifiedSentence = clientSocket.recv(1024)
        except timeout: # socket.timeout
            print(i)
            loss += 1
        # print(modifiedMessage.decode())
        print(f'PING: {i}    RTT: {process_time() - start:0.5f} sec')
        i += 1
        clientSocket.close()
    print(f'packet loss: {loss / shot}%')


if __name__ == '__main__':
    ping(10)
    # ping(1000)


