import socket, time
import numpy as np
from scipy.io.wavfile import write

TCP_IP = '172.25.79.180' # 172.25.98.219 Saad's IP
TCP_PORT = 4000
BUFFER_SIZE = 1024
time.sleep(2)
MESSAGE = ("a")
bin_data = bin(int.from_bytes(MESSAGE.encode(), 'big'))
msg = np.array(list(bin_data[2:]), dtype = 'uint8')
print(msg)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendall(msg)
s.sendall(msg)
msg = s.recv(BUFFER_SIZE)
s.close()

print("Data sent: ", msg)
