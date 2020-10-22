from socket import *
from time import process_time


SERVER_NAME = 'localhost'
SERVER_PORT = 12000
MESSAGE = 'PING'

def ping(shot):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    loss = 0
    for i in range(1, shot + 1):
        start = process_time()
        try:
            clientSocket.sendto(MESSAGE.encode(), (SERVER_NAME, SERVER_PORT))
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        except timeout: # socket.timeout
            print(i)
            loss += 1
        # print(modifiedMessage.decode())
        print(f'PING: {i}    RTT: {process_time() - start:0.5f} sec')
        i += 1
    print(f'packet loss: {loss / shot}%')


if __name__ == '__main__':
    ping(10)
    ping(1000)


