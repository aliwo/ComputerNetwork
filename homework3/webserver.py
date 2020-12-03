from socket import *


class Webserver:


    def __init__(self, port, connection):
        self.port = port

        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('', port))
        serverSocket.listen(connection)

        self.serverSocket = serverSocket

    def run_forever(self):
        while True:
            print('The server is ready to receive')

            # Set up a new connection from the client
            connectionSocket, addr = self.serverSocket.accept()

            host, _ = connectionSocket.getpeername()
            # If an exception occurs during the execution of try clause
            # the rest of the clause is skipped
            # If the exception type matches the word after except
            # the except clause is executed
            try:
                # Receives the request message from the client
                message = connectionSocket.recv(2048).decode()
                print(message)

                # Extract the path of the requested object from the message
                # The path is the second part of HTTP header, identified by [1]
                filename = message.split()[1]
                print(filename)

                # Because the extracted path of the HTTP request includes
                # a character '\', we read the path from the second character
                myfile = open(filename[1:], 'rb')

                # Store the entire content of the requested file in a temporary buffer
                response = myfile.read()
                myfile.close()

                # Send the HTTP response header line to the connection socket
                header = 'HTTP/1.1 200 OK\n'

                if (filename.endswith(".jpg")):
                    filetype = 'image/jpg'
                elif (filename.endswith(".gif")):
                    filetype = 'image/gif'
                elif (filename.endswith(".mp4")):
                    filetype = 'video/mp4'
                elif (filename.endswith(".wmv")):
                    filetype = 'video/x-ms-wmv'
                else:
                    filetype = 'text/html'

                header += 'Content-Type: ' + str(filetype) + '\n\n'
                print(header)

                if not filename.endswith(".mp4"):
                    connectionSocket.send(header.encode())
                    connectionSocket.send(response)
                    connectionSocket.close()
                else:
                    # mp4 에 대해서, chrome 의 괴의한 행동에 대응 합니다.
                    # https://support.google.com/chrome/thread/25510119?hl=en
                    # mp4 를 요청하는 경우 chrome 은 다음과 같이 행동합니다.
                    # 1. 전체 파일을 요청합니다.
                    # 2. 헤더만 받자마자 커넥션을 끊어버립니다. (만약 서버가 전체 영상을 계속 보낼 경우 패킷은 전부 lost)
                    # 3. 이후 필요에 따라서 영상을 조금씩 받습니다.
                    # 2번 때문에, 영상을 보낼 때 header 를 먼저 보내고 response 를 보내려 하는 순간
                    # BrokenPipe Error 가 발생하게 됩니다. 따라서 mp4를 보낼때는 해당 error 를 캐치해 줍니다.
                    try:
                        connectionSocket.send(header.encode())
                        connectionSocket.send(response)
                        connectionSocket.close()
                    except IOError:
                        pass

            except IOError as e:
                header = 'HTTP/1.1 404 Not Found\n\n'
                response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode()

                print(header)
                connectionSocket.send(header.encode())
                connectionSocket.send(response)
                connectionSocket.close()

        serverSocket.close()
        sys.exit()


