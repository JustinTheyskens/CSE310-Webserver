from socket import *
serverHost = 'localhost'
serverPort = 8000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((serverHost, serverPort)) #bind to ip, port
serverSocket.listen(1) # one client at a time
print('listening to port', serverPort)
while True:
    connectionSocket, addr = serverSocket.accept() #accept connection
    print('connecting to: ', str(addr))
    try:
        request = connectionSocket.recv(1024).decode()

        print(request)
        filename = request.split()[1]
        file = filename.replace('/', '')
        r = open(file)
        print(file)
        output = r.read()
        response = b'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'

        connectionSocket.send(response)

        for i in range(0, len(output)):
            connectionSocket.send(str.encode(output[i]))

    except(IOError,  IndexError) as e:
        print(e)
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()



