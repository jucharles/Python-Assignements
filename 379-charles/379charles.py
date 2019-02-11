
import socket
def test():
    serverPort = 6969
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#defines socket using ipv4 and tcp
    serverSocket.bind(('',serverPort))#binds host and port
    serverSocket.listen()#listens to only one connection
    print("Now listening on",serverPort)
    while True:
        print("ready to serve")#lets me know while statement has been inititied
        connectionSocket,addr = serverSocket.accept()#creates a socket to accept client
        try:
            print('Now serving:', addr)
            message = connectionSocket.recv(1024)
            print(message)
            filename = message.split()[1]#gets file from client
            print(filename)
           
            f = open(filename[1:])
           
            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf-8')) #http header line sent to socket
            for line in f.read():#reads contexts of file 
                connectionSocket.sendall(line.encode('utf-8'))
           
           
            connectionSocket.close()
        except IOError: #sends error if no file is found
            pass
            print ("404 Not Found")
            connectionSocket.send("""HTTP/1.1 404 Not Found\r\n""".encode('utf-8'))
         
        break
    pass
if __name__ =="__main__":
   test()