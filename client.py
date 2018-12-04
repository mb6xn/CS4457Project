import socket, time
import numpy as np
from scipy.io.wavfile import write

TCP_IP = '172.25.79.180' # 172.25.98.219 Saad's IP
TCP_PORT = 4000
BUFFER_SIZE = 1024
time.sleep(2)
MESSAGE = ("a")  #let's read in num=len(message) bytes because ASCII values go up to 127, then right shift by 1.
file = open("key.txt", "rb") #works for larger strings
num=len(MESSAGE)
key= bin(int.from_bytes(file.read(num), 'big')>>1)[2:]
#print("Key:       "+key)

bin_data = (bin(int.from_bytes(MESSAGE.encode(), 'big')))[2:]
#print("Data:      "+bin_data)

encrypt = bin(int(bin_data,2) ^ int(key,2))[2:].zfill(len(key))  #same for decryption
#print("Encrypted: "+encrypt)
msg = np.array(list(encrypt), dtype = 'uint8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendall(msg)
s.sendall(msg)
msg = s.recv(BUFFER_SIZE)
s.close()

print("Data sent: ", msg)