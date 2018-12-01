import socket
import numpy as np
import sounddevice as sd
import pylab as plt
from rtlsdr import RtlSdr
import scipy.signal as signal


TCP_IP = ''
TCP_PORT = 4000
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)

conn, addr = s.accept()
print ('Connection address:', addr)

while 1:
    msg = conn.recv(BUFFER_SIZE)
    if not msg: break
    print ("received data:", msg)
    conn.sendall(msg)  # echo

conn.close()
