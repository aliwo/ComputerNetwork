# Import socket module
from socket import * 
import sys # In order to terminate the program

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789


# Bind the socket to server address and server port
serverSocket.bind(('', serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections

while True:
        print('The server is ready to receive')

        # Set up a new connection from the client
        connectionSocket, addr = serverSocket.accept()

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
                myfile = open(filename[1:],'rb')

	        # Store the entire contenet of the requested file in a temporary buffer
                response = myfile.read()
                myfile.close()
		
		# Send the HTTP response header line to the connection socket
                header = 'HTTP/1.1 200 OK\n'

                if(filename.endswith(".jpg")):
                        filetype = 'image/jpg'
                elif(filename.endswith(".mp4")):
                        filetype = 'video/mp4'
                else:
                        filetype = 'text/html'

                header += 'Content-Type: '+str(filetype)+'\n\n'
                print(header)

                connectionSocket.send(header.encode())
                connectionSocket.send(response)
                connectionSocket.close()

        except IOError:
                header = 'HTTP/1.1 404 Not Found\n\n'
                response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode() 

                print(header)
                connectionSocket.send(header.encode())
                connectionSocket.send(response)
                connectionSocket.close()
        
serverSocket.close()
sys.exit()
