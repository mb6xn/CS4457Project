#Step 1 of Final Exam.  Note: Web server is running on localhost:8555 right now.

from socket import *
serverPort = 8555
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while(1):
    connectionSocket, addr = serverSocket.accept()
    #print(addr[0])
    connectionSocket.send(("HTTP/1.1 200 OK\n" +"Content-Type: text/html\n" +"\r\n"+"<html><body>Secret black site </body></html>\n").encode())
    connectionSocket.send(addr[0].encode())

connectionSocket.close()

