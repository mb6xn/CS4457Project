import socket
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

#from rtlsdr import *


TCP_IP = '172.25.79.75' # Saad's IP
TCP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = ("this is the pepsi and saad is very sexy")
bin_data = bin(int.from_bytes(MESSAGE.encode(), 'big'))
msg = np.array(list(bin_data[2:]), dtype = 'uint8')
print (msg)
sd.play(msg, 44100)
#broadcast message on FM88.7

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendall(msg)
msg = s.recv(BUFFER_SIZE)
s.close()

print ("sent data:", msg)
