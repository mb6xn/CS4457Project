# import socket
# from client import client
#
# server = RtlSdrTcpServer(hostname='192.168.1.100', port=12345)
# server.run_forever()
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = "127.0.0.1"
# port = 4000
# s.connect((host,port))
#
# def ts(str):
#    s.send('e'.encode())
#    data = ''
#    data = s.recv(1024).decode()
#    print (data)
#
# while 2:
#    r = input('enter')
#    ts(s)
#
# s.close ()
