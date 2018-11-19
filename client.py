import socket
import sys
from rtlsdr import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 4000
serversocket.bind((host, port))

# client class
class client():
    def __init__(self, socket, address):
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            print('Client sent:', self.sock.recvfrom(1024).decode())
            self.sock.send('who dis')

# server listening to FM87.7 on port 4000
serversocket.listen(4)
print ('Server started and listening')
while 1:
    print('test')
    try:
        print('test')
        (clientsocket, address) = serversocket.accept()
        client = RtlSdrTcpClient(hostname='127.0.0.1', port=4000)
        client.center_freq = 87.7e6
        data = client.read_samples()
        print ("Connection Made")
        print(data)
        serversocket.close()
    except KeyboardInterrupt:
        print ('', 'Interrupted')
        sys.exit(0)
