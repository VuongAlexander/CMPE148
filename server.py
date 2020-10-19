# import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
#bindIP = "128.238.251.26"
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print('Message is: ', message)
        filename = message.split()[1]
        print('File name is: ', filename)
        f = open(filename[1:])
        outputdata = f.readlines()
        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n')
        connectionSocket.send('\r\n')
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        print('Success! File sent!')
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n", "UTF-8"))
        connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n", "UTF-8"))
        # Close client socket
        connectionSocket.close()
serverSocket.close()
# Terminate the program after sending the corresponding data
sys.exit()
