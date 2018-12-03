import socket
import numpy as np
import pylab as plt
from rtlsdr import RtlSdr
import scipy.signal as signal


TCP_IP = '127.0.0.1'
TCP_PORT = 4000
BUFFER_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)

conn, addr = s.accept()
print ('Connection by', addr)

while 1:
    msg = conn.recv(BUFFER_SIZE)
    if not msg: break
    print ("Received Data:", msg)
    conn.sendall(msg)  # echo

conn.close()
